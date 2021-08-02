n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
res = []
total_sum = 0

for i in range(m):
    data = list(map(int, input().split()))
    if data[0] == 1:
        a[data[1] - 1] = data[2] - total_sum
    else:
        if data[0] == 2:
            total_sum += data[1]
        else:
            res.append(str(a[data[1] - 1] + total_sum))

print('\n'.join(res))
