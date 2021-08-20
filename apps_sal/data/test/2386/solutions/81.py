n = int(input())
a = list(map(int, input().split()))
b = a
for bb in range(n):
    b[bb] -= bb + 1
b.sort()
if n % 2 == 1:
    c = b[n // 2]
    d = c
else:
    c1 = b[n // 2 - 1]
    c2 = b[n // 2]
    c = c1 + c2
    if c % 2 == 1:
        c = c // 2
        d = c + 1
    else:
        c = c // 2
        d = c
res1 = 0
res2 = 0
for i in range(n):
    res1 += abs(b[i] - c)
for j in range(n):
    res2 += abs(b[j] - d)
print(min(res1, res2))
