n, m = list(map(int, input().split()))
s = []
s1 = []
for i in range(n):
    a, b = list(map(int, input().split()))
    s.append(a)
    s1.append(a - b)
x = sum(s)
s1.sort()
ans = 0
while x > m and len(s1) > 0:
    ans += 1
    x -= s1[-1]
    s1.pop()
if x > m:
    print(-1)
else:
    print(ans)
