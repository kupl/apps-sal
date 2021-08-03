s = str(input())

current = ord('a')

n = len(s)

ans = ''

for i in range(n):
    if ord(s[i]) <= current and current < 123:
        ans += chr(current)
        current += 1
    else:
        ans += s[i]

if current == 123:
    print(ans)

else:
    print(-1)
