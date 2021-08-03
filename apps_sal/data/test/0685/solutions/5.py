n, h = map(int, input().split(' '))
x = []
for i in range(n):
    x1, x2 = map(int, input().split(' '))
    x.append([x1, x2])

cur = 1
S = 0
i = 0
res = 0
while cur < n:
    # print()
    while S <= h and i < n - 1:
        i += 1
        S += x[i][0] - x[i - 1][1]
    #print(S, i, res)
    if S > h:
        S -= (x[i][0] - x[i - 1][1])
        i -= 1
    # elif i == n - 1:
        #i -= 1
    #print(S, i)
    if S < h:
        res1 = x[i][1] + h - S - x[cur - 1][0]
    else:
        res1 = x[i][0] - x[cur - 1][0]
    res = max(res, res1)
    # print(res)
    S -= (x[cur][0] - x[cur - 1][1])
    cur += 1

res = max(res, x[-1][1] - x[-1][0] + h)
print(res)
