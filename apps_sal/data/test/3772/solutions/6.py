a, b = map(int, input().split())
s = 0
while b:
    s += a // b
    a, b = b, a % b
print(s)
