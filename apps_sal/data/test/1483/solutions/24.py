n = int(input())
inp = [int(i) - 1 for i in input().split()]
ans = []
for i in range(n):
    a = [False] * n
    ii = i
    while not a[ii]:
        a[ii] = True
        ii = inp[ii]
    ans.append(ii + 1)
print(*ans)
