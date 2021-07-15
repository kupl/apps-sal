n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

res = 0
tmp1 = 0
for i in range(n):
    tmp1 += a1[i]
    tmp2 = 0
    for j in range(i, n):
        tmp2 += a2[j]
    res = max(res, tmp1+tmp2)

print(res)

