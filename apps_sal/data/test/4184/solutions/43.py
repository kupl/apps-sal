N = int(input())
W = list(map(int, input().split()))
L = []
S1 = S2 = 0

for i in range(len(W)):
    S1 = sum(W[:i])
    S2 = sum(W[i:])

    L.append(abs(S1 - S2))

print(min(L))
