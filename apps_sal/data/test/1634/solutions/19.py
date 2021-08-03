c = [int(x) for x in input().split()]
n, m = (int(x) for x in input().split())
a = b = 0
for x in input().split():
    x = int(x)
    a += min(x * c[0], c[1])
for x in input().split():
    x = int(x)
    b += min(x * c[0], c[1])
print(min(c[3], min(c[2], a) + min(c[2], b)))
