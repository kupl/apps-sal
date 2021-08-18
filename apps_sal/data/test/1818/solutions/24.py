n = int(input())
lis = list(map(int, input().split()))
ans = [0] * (n)
for i in range(n):
    k = lis[i]
    c = 0
    while k > 0:
        if k % 2 != 0:
            c += 1
        k = k // 2
    ans[i] = c
ans.sort()
c = 1
fin = 0
for i in range(1, n):
    if ans[i - 1] == ans[i]:
        c += 1
    else:
        fin += ((c * (c - 1)) // 2)
        c = 1
fin += ((c * (c - 1)) // 2)
print(fin)
