n = int(input())
s = input()

if n % 2 == 1 or s.count('(') != s.count(')'):
    print(-1)
    return

a = 0
nl = -1
nr = -1
ans = 0
for i in range(n):
    if s[i] == '(':
        a += 1
    else:
        a -= 1
    if a < 0:
        if nl <= -1:
            nl, nr = i, i + 1
        else:
            nr = i + 1
    else:
        if nl != -1:
            ans += nr - nl + 1
            nl, nr = -1, -1
print(ans)
