n = int(input())
s = input()
ans = 0
for i in range(n, len(s), n):
    if s[i - 3:i] in ('aaa', 'bbb'):
        ans += 1
print(ans)
