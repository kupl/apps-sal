a, b, x = map(int, input().split())

l = a // x + 1
if a % x == 0:
    l -= 1

r = b // x

print((r - l) + 1)
