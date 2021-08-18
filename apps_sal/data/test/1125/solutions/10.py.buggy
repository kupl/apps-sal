n = int(input())
a, b, *L = map(int, input().split())
x = 0
for l in L:
    x ^= l
s = a + b
if s - x < 0 or (s - x) % 2:
    print(-1)
    return
d = (s - x) // 2
if d & x:
    print(-1)
    return
if d > a:
    print(-1)
    return
for i in range(50, -1, -1):
    if (x >> i) & 1 and d | (1 << i) <= a:
        d |= 1 << i
if d == 0:
    print(-1)
    return
ans = a - d
print(ans)
