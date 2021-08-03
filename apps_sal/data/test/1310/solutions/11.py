n = int(input())
ans = -1
tab = list(map(int, input(). split()))
for i in range(n):
    foo = 0
    for j in range(i, n):
        foo ^= tab[j]
        ans = max(ans, foo)
print(ans)
