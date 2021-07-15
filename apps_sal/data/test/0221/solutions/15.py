n, k = map(int, input().split())
for i in range(k + 1):
    #print(i + 1 + k)
    ost = n - (i + 1 + k)
    ost = ost % (k * 2 + 1)
    #print(ost)
    if k + 1 <= ost or ost == 0:
        ans = []
        for j in range(i, n, k * 2 + 1):
            ans.append(j + 1)
    #print(ans)
if k == 0:
    ans = [i + 1 for i in range(n)]
print(len(ans))
print(*ans)
