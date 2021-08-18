N = int(input())
K = int(input())
x_list = list(map(int, input().split()))

sum_distance = 0

for x in x_list:
    if x < K - x:
        sum_distance += 2 * x
    else:
        sum_distance += 2 * (K - x)

print(sum_distance)
