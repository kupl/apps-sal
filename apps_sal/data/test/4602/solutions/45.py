N = int(input())
K = int(input())
x = list(map(int, input().split()))
sum_min = 0

for p in x:
    a = 2 * p
    b = 2 * abs(K - p)
    if a >= b:
        sum_min += b
    elif a < b:
        sum_min += a

print(sum_min)
