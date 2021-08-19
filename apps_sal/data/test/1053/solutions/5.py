n = int(input())
level = 1
res = 0
while n > 1:
    res += level * (n // 2)
    level *= 2
    n = n // 2 + n % 2
print(res)
