n, a = map(int, input().split())
t = [0] + list(map(int, input().split()))
ans = t[a]
for i in range(1, max(a, n - a + 1)):
    if a - i > 0 and a + i <= n:
        if t[a - i] == t[a + i]: ans += t[a - i] + t[a + i]
    elif a - i > 0: ans += t[a - i]
    else: ans += t[a + i]

print(ans)
