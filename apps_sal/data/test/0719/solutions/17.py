import sys
f = sys.stdin
d = [[0] * 11 for _ in range(11)]
d[0][0] = 1
for i in range(10):
    for j in range(11):
        for k in range(10):
            if j + k <= 10:
                d[i + 1][j + k] += d[i][j]
target = int(f.readline())
tt = target
target -= 1
val = 10
ans = ''
for i in range(10):
    ii = 9 - i
    for j in range(val + 1):
        if j == 10:
            continue
        jj = val - j
        if d[ii][jj] <= target:
            target -= d[ii][jj]
        else:
            val = jj
            ans += str(j)
            break
print(int(ans))
