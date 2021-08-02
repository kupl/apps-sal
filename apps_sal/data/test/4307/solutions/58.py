# input
N = int(input())

# calculate
cnt = 0
for i in range(1, N + 1, 2):
    divisor = 0
    # count divisors
    for j in range(1, i + 1):
        if i % j == 0:
            divisor += 1
    # check number of divisors
    if divisor == 8:
        cnt += 1

# output
print(cnt)
