s = input()
n = len(s)
ans = ''
if n % 2 == 0:
    now = n // 2 - 1
else:
    now = n // 2
for i in range(n):
    if i % 2 != 0:
        ans += s[now + i]
        now += i
    else:
        ans += s[now - i]
        now -= i
print(ans)

