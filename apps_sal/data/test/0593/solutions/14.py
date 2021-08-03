n, m = map(int, input().split())
b = [0] * (n + 1)
for i in range(m):
    a = list(map(int, input().split()))
    max_ = -1
    index_max = -1
    for j in range(len(a)):
        if (a[j] > max_):
            max_ = a[j]
            index_max = j
    b[index_max] += 1
max_ = -1
index_max = -1
for i in range(len(b) - 1):
    if (b[i] > max_):
        max_ = b[i]
        index_max = i
print(index_max + 1)
