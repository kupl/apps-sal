n = int(input())
x = list(map(int, input().split()))
x_sort = sorted(x)
half_l = x_sort[(n - 1) // 2]
half_r = x_sort[(n) // 2]

for i in range(n):
    if x[i] <= half_l:
        print(half_r)
    else:
        print(half_l)
