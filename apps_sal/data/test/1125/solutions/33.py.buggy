n = int(input())
l = list(map(int, input().split()))

x = 0
s = l[0] + l[1]
for i in l[2:]:
    x ^= i
if x > s or (s - x) % 2 or ((s - x) // 2) & x:
    print(-1)
    return
a = (s - x) // 2
if a > l[0]:
    print(-1)
    return
for i in range(50, -1, -1):
    if 1 << i & x:
        if a + (1 << i) <= l[0]:
            a += 1 << i
if a == 0:
    print(-1)
else:
    print(l[0] - a)
