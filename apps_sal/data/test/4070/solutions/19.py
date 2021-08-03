a = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1, 1, 2, 0, 1, 0, 0]
x = int(input())
b = 0
if x == 0:
    b += 1
while x:
    b += a[x % 16]
    x //= 16
print(b)
