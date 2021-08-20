(n, k) = map(int, input().split())
a = 1
b = k
while n >= b:
    b = b * k
    a += 1
print(a)
