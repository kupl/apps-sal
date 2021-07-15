a, b = map(int, input().split())
val = 0
while b > 0:
    a, b, val = b, a % b, val + a // b
print(val)
