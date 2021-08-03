import math

n = int(input())
lst = [int(i) for i in input().split()]
lst.sort()
total = sum(lst)
more = total - math.floor(total / n) * n
result = [math.floor(total / n) for i in range(n)]
for i in range(n - more, n):
    result[i] += 1
sum_move = 0
for (ori, res) in zip(lst, result):
    if ori > res:
        sum_move = sum_move + (ori - res)
print(sum_move)
