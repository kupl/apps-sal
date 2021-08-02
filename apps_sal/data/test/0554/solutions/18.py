def get_line(func=int, sym=' '):
    return [func(i) for i in input().split(sym)]


n, m = get_line()
a = [0] + get_line()
S = [0] * (n + 1)
for i in range(n):
    S[i + 1] = S[i] + a[i + 1]
ans = 0
for i in range(m):
    l, r = get_line()
    mood = S[r] - S[l - 1]
    if mood > 0:
        ans += mood
print(ans)
