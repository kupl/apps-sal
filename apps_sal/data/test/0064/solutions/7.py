(n, k) = map(int, input().split())
s = input()
f = True
for i in range(n):
    if s.count(s[i]) > k:
        f = False
if f:
    print('YES')
else:
    print('NO')
