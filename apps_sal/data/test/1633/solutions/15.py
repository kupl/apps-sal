import sys
nmk = list(map(int, sys.stdin.readline().split()))
n = nmk[0]
m = nmk[1]
k = nmk[2]
a = [[0 for i in range(m + 2)] for j in range(n + 2)]
rs = 0
for i in range(k):
    tt = list(map(int, sys.stdin.readline().split()))
    a[tt[0]][tt[1]] = 1
    if rs == 0:
        if a[tt[0]][tt[1] + 1] == 1:
            if (a[tt[0] - 1][tt[1]] == 1 and a[tt[0] - 1][tt[1] + 1] == 1) or (a[tt[0] + 1][tt[1]] == 1 and a[tt[0] + 1][tt[1] + 1] == 1):
                rs = i + 1

        if a[tt[0]][tt[1] - 1] == 1:
            if (a[tt[0] - 1][tt[1]] == 1 and a[tt[0] - 1][tt[1] - 1] == 1) or (a[tt[0] + 1][tt[1]] == 1 and a[tt[0] + 1][tt[1] - 1] == 1):
                rs = i + 1
print(rs)
