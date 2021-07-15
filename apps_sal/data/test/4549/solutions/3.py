h, w = list(map(int, input().split()))
S = [input() for i in range(h)]
for i, T in enumerate(S):
    for j, t in enumerate(T):
        if t == "#":
            flag = 0
            if j > 0:
                if T[j - 1] == "#":
                    flag += 1
            if j < w - 1:
                if T[j + 1] == "#":
                    flag += 1
            if i > 0:
                if S[i - 1][j] == "#":
                    flag += 1
            if i < h - 1:
                if S[i + 1][j] == "#":
                    flag += 1
            if flag == 0:
                print("No")
                return
print("Yes")

