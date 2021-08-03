n = int(input())
L = list(map(int, input().split()))

x = min(L)

prv = -1
ans = 10**100
for i in range(n):
    if (L[i] == x):
        if (prv != -1):
            ans = min(ans, i - prv)
        prv = i
print(ans)
