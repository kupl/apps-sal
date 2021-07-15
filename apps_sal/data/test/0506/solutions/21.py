count = 0
a, b = list(map(int, input().split(" ")))
while a > 0 and b > 0:
    count += a//b
    x = b
    b = a % b
    a = x
print(count)
