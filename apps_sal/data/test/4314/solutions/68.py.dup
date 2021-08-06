import numpy as np

H, W = map(int, input().split())
hw = np.array([list(input()) for _ in range(H)])

gyo = np.all(hw == ".", axis=1)
retu = np.all(hw == ".", axis=0)

for i in range(H):
    if not gyo[i] == True:
        for j in range(W):
            if not retu[j] == True:
                print(hw[i][j], end="")
        print()
