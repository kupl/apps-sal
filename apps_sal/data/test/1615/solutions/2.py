n, k = map(int, input().split())
s = 0
for i in range(n):
    l, r = map(int, input().split())
    s += l - r
print((s - n) % k)
