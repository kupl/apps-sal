n, a = [int(x) for x in input().split()]
val = [int(x) for x in input().split()]
vsum = 0
for i in val:
    vsum += i
ans = [0] * n
for i in range(n):
    if a - (vsum - val[i]) > 1:
        ans[i] += a - (vsum - val[i]) - 1
    if val[i] > a - n + 1:
        ans[i] += val[i] - (a - n + 1)
for i in ans:
    print(i, end=' ')
