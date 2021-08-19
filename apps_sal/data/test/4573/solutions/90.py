n = int(input())
x = list(map(int, input().split()))
for i in range(n):
    x[i] = [x[i], i]
x.sort(key=lambda x: x[0])
for i in range(n):
    if i < n // 2:
        x[i] += [x[n // 2][0]]
    else:
        x[i] += [x[n // 2 - 1][0]]
# x[i] = [value, init_index, b_i]
x.sort(key=lambda x: x[1])
for i in range(n):
    print(x[i][2])
