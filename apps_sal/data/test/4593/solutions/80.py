n = int(input())
a = {1}
for b in range(2, n):
    p = 2
    x = b ** p
    while x <= n:
        a.add(x)
        x = b ** p
        p += 1
print(max(a))
