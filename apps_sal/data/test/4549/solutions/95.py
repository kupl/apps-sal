import re
import copy


def accept_input():
    H, W = list(map(int, input().split()))
    S = []
    for _ in range(H):
        S.append(input())
    return H, W, S


def process(s):
    if s == "
      return 1
    else:
        return 0


H, W, S = accept_input()
arr1 = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, 1), (0, -1)]
arr = [(-1, 0), (1, 0), (0, 1), (0, -1)]
new_S = copy.deepcopy(S)
g = 0
b = 0
for i in range(H):
    for j in range(W):
        if new_S[i][j] == "
          bl = 0
           for idou in arr:
                if i + idou[0] == -1 or i + idou[0] == H:
                    continue
                elif j + idou[1] == -1 or j + idou[1] == W:
                    continue
                else:
                    if new_S[i + idou[0]][j + idou[1]] == "
                      bl = 1
            if bl != 1:
                b = 1
                break
    if b == 1:
        break
if b == 1:
    print("No")
else:
    print("Yes")
