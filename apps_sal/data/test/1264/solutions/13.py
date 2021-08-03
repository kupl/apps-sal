n = int(input())
I = list(map(int, input().split()))
d = []
for val in I:
    d.append(val)
res = 0
for i in range(0, n):
    for j in range(i, n):
        cnt = 0
        for k in range(0, n):
            if k >= i and k <= j:
                cnt = cnt + 1 - d[k]
            else:
                cnt = cnt + d[k]
        if cnt > res:
            res = cnt
print(res)
