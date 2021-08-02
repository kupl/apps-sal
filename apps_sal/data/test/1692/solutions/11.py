3

s = input()
# s = '124'
n = len(s)

ans = 0

for i in reversed(list(range(1, n))):
    if int(s[i]) % 2 == 0:
        if int(s[i - 1:i + 1]) % 4 == 0:
            ans += i
        if int(s[i]) % 4 == 0:
            ans += 1

if int(s[0]) % 4 == 0: ans += 1

print(ans)
