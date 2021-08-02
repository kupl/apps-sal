n = int(input())

x = list(map(int, input().split()))
x_sorted = sorted(x)
med_low = x_sorted[(n // 2) - 1]
med_upper = x_sorted[(n // 2)]

for i in range(n):
    if x[i] <= med_low:
        print(med_upper)
    else:
        print(med_low)
