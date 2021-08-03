n, a, b = map(int, input().split())
sum = 0
sum_n = 0
for num in range(1, n + 1):
    num2 = num
    sum_n = 0
    while num > 0:
        sum_n += num % 10
        num //= 10
    if sum_n >= a and sum_n <= b:
        sum += num2
print(sum)
