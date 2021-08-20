(h, w, d) = list(map(int, input().split()))
index = [-1] * (h * w)
for i in range(h):
    a = list(map(int, input().split()))
    for j in range(len(a)):
        index[a[j] - 1] = (i + 1, j + 1)
data = [[] for _ in range(d)]
for i in range(1, d + 1):
    num = i
    (x, y) = index[num - 1]
    data[i - 1].append(0)
    num += d
    while num <= h * w:
        (x_new, y_new) = index[num - 1]
        data[i - 1].append(abs(x - x_new) + abs(y - y_new) + data[i - 1][-1])
        (x, y) = (x_new, y_new)
        num += d
q = int(input())
for i in range(q):
    (l, r) = list(map(int, input().split()))
    index_data = l % d - 1
    r = (r - 1) // d
    l = (l - 1) // d
    print(data[index_data][r] - data[index_data][l])
