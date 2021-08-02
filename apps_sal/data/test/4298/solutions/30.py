a, b = map(int, input().split())
b = b * 2 + 1
c = 0
while a > 0: a -= b; c += 1
print(c)
