(n, k) = map(int, input().split())
for i in range(k + 1):
    ost = n - (i + 1 + k)
    ost = ost % (k * 2 + 1)
    if k + 1 <= ost or ost == 0:
        ans = []
        for j in range(i, n, k * 2 + 1):
            ans.append(j + 1)
if k == 0:
    ans = [i + 1 for i in range(n)]
print(len(ans))
print(*ans)
