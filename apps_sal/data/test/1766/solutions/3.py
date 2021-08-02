n = int(input())
a = list(map(int, input().split()))
b = [0, 0]
c = 0
while n:
    if a[0] > a[n - 1]:
        b[c] += a[0]
        a = a[1:n]
    else:
        b[c] += a[n - 1]
        a = a[0:n - 1]
    c = 1 - c
    n -= 1
print("%d %d" % (b[0], b[1]))
