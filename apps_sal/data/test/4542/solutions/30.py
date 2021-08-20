s = list(input())
n = len(s)
b = False
if s[0] == 'B':
    b = True
ans = 0
for i in range(1, n):
    if b and s[i] == 'W':
        b = False
        ans += 1
    elif not b and s[i] == 'B':
        b = True
        ans += 1
print(ans)
