n, k = list(map(int, input().split()))

s = input()

L = []
for i in range(n):
    L.append(s[i])

L[k - 1] = str.lower(L[k - 1])
ans = str()
for i in range(n):
    ans += L[i]
print(ans)
