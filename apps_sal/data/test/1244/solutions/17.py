n = int(input())
s = [0] * 1001
f = True
t = list(map(int, input().split()))
for i in range(n):
    a = t[i]
    s[a] += 1
for i in range(1001):
    if s[i] > (n + 1) // 2:
        f = False
if f:
    print('YES')
else:
    print('NO')
