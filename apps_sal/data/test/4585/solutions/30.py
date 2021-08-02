x = int(input())
n = 1
while n * (n + 1) // 2 < x:
    n += 1
print(n)
