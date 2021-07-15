read = lambda: list(map(int, input().split()))
n, a = read()
t = list(read())
ans = 0
for d in range(n):
    i, j = a - d - 1, a + d - 1
    if i == j: ans += t[i]
    elif i >= 0 and j < n and t[i] == t[j]: ans += t[i] + t[j]
    elif i < 0 and j < n: ans += t[j]
    elif i >= 0 and j >= n: ans += t[i]
print(ans)

