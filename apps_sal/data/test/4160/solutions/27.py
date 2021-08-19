x = int(input())
y = 100
n = 0
while y < x:
    n += 1
    y += y // 100
print(n)
