def get_input_list():
    return list(map(int, input().split()))


n, m = get_input_list()
a = get_input_list()
b = get_input_list()
x = int(input())
sa = [0]

for i in range(1, n + 1):
    s = sum(a[:i])
    mi = s
    j = i
    while (j < n):
        s = s - a[j - i] + a[j]
        if mi > s:
            mi = s
        j += 1
    sa.append(mi)

sb = [0]
for i in range(1, m + 1):
    s = sum(b[:i])
    mi = s
    j = i
    while (j < m):
        s = s - b[j - i] + b[j]
        if mi > s:
            mi = s
        j += 1
    sb.append(mi)

r = 0
for i in range(n + 1):
    for j in range(m + 1):
        if sa[i] * sb[j] <= x:
            if i * j > r:
                r = i * j

print(r)
