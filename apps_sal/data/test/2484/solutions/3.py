n = int(input())
al = list(map(int, input().split()))
al.append(0)
res = 0
r = 0
x = 0
y = 0
for l in range(n):
    while x == y and r <= n:
        x += al[r]
        y = y ^ al[r]
        r += 1
    r -= 1
    x -= al[r]
    y = y ^ al[r]
    res += r - l
    x -= al[l]
    y = y ^ al[l]
    if l == r:
        r += 1
print(res)
