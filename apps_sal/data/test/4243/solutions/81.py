n = int(input())
sum = 0
while n >= 500:
    n -= 500
    sum += 1000
while n >= 5:
    n -= 5
    sum += 5
print(sum)
