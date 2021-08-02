s = input()
n = len(s)
was = [0, 0, 0, 0, 0]
ans = 1
cnt = 10
k = []
e = set(k)

for i in range(n):
    if (s[i] >= 'A' and s[i] <= 'J' and s[i] not in e):
        e.add(s[i])
        ans *= cnt
        cnt -= 1
    else:
        if (s[i] == '?'):
            ans *= 10

if (s[0] >= 'A' and s[0] <= 'J'):
    ans = ans // 10 * 9

if (s[0] == '?'):
    ans = ans // 10 * 9

print(ans)
