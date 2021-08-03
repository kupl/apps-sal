N = int(input())

sum_num = 0
for i in range(1, N + 1):
    x = N // i
    m = (x * (x + 1) // 2) * i
    sum_num += m

print(sum_num)
