
n, a, b = map(int, input().split())
sum = 0

for i in range(1, n + 1):
    tmp_sum = 0
    for j in str(i):
        tmp_sum += int(j)
    if a <= tmp_sum and tmp_sum <= b:
        sum += i

print(sum)
