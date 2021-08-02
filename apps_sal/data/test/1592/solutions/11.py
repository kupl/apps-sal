n = int(input())
a, b = map(int, input().split())
l = b
x = a
q = 0
m = 0
m = max(m, l)
for i in range(n - 1):
    a, b = map(int, input().split())
    l -= (a - x)
    l = max(l, 0)
    l += b
    m = max(m, l)
    x = a
print("{} {}".format(x + l, m))
