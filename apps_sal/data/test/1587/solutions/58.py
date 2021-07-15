N = int(input())
s = str(input())

a = 0
b = 0

for i in range(N):
    if s[i] == 'R':
        a = a + 1
ans = max(a,b)
for i in range(N):
    if s[i] == 'R':
        a = a - 1
    else:
        b = b + 1
    now = max(a,b)
    ans = min(ans, now)
print(ans)

