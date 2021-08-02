s = input()

n = (len(s) + 1) // 2

ans = ''

for i in range(n):
    ans += s[2 * i]

print(ans)
