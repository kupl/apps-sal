n,a,b,c,d = list(map(int, input().split()))
num = 0
i = 0
while n > i:
    i += 1
    if i + b - c < 1 or i + b - c > n:
        continue
    if i + a - d < 1 or i + a - d > n:
        continue
    if i + a - d + b - c  < 1 or i + a - d + b - c > n:
        continue
    num += 1
print(num * n)

