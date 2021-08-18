
n = int(input())
s = input()

t = ''
cnt = 0
while len(s) > 0:
    t += s[0]
    s = s[1:]
    if len(t) >= 3 and t[-3:] == 'fox':
        cnt += 1
        t = t[:-3]

ans = n - 3 * cnt
print(ans)
