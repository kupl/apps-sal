import numpy as np

H, W = list(map(int, input().split()))
G = []
for _ in range(H):
    G.append([1 if x == '.' else 0 for x in input()])
G = np.array(G)
HWOnes = np.ones_like(G)

North = np.cumsum(np.ones_like(G), axis=0)
North *= (1 - G)
North = np.maximum.accumulate(North, axis=0) * G

South = np.cumsum(np.ones_like(G), axis=0)
South *= np.flipud(1 - G)
South = np.maximum.accumulate(South, axis=0)
South = (H - np.flipud(South)) * G

West = np.cumsum(np.ones_like(G), axis=1)
West *= (1 - G)
West = np.maximum.accumulate(West, axis=1) * G

East = np.cumsum(np.ones_like(G), axis=1)
East *= np.fliplr(1 - G)
East = np.maximum.accumulate(East, axis=1)
East = (W - np.fliplr(East)) * G

print((np.amax(South - North + East - West - 1)))
