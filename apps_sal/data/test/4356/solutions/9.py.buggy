import sys
n, m = map(int, input().split())
la = [input() for _ in range(n)]
lb = [input() for _ in range(m)]
for i in range(n - m + 1):
    for j in range(n - m + 1):
        cnt = 0
        for k in range(m):
            for l in range(m):
                if la[i + k][j + l] == lb[k][l]:
                    cnt += 1
        if cnt == m**2:
            print("Yes")
            return
print("No")
