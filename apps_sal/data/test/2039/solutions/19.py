
def is_extrema(a, i):
    return a[i - 1] < a[i] > a[i + 1] or a[i - 1] > a[i] < a[i + 1]


_ = input()

arr = [int(x) for x in input().split(' ')]


num_extrema = 0
for i in range(1, len(arr) - 1):
    if is_extrema(arr, i):
        num_extrema += 1

print(num_extrema)
