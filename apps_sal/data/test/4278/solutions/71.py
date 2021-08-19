n = int(input())
s = {}
ans = 0
for i in range(n):
    a = tuple(sorted(input()))
    if a in s:
        s[a] += 1
    else:
        s[a] = 1
for i in s.values():
    ans += i * (i - 1) // 2
print(ans)
