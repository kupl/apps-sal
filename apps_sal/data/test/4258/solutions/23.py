a, b, t = list(map(int, input().split()))
sum = 0
x = a
while x <= t + 0.5:
    sum += b
    x += a
print(sum)
