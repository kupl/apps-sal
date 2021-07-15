n = int(input())
a = [n]
index = 0

for i in range(1, 1000000):
    if a[i - 1] % 2 == 0:
        m = a[i - 1] / 2
    else:
        m = 3 * a[i - 1] + 1
    if m in a:
        index = i + 1
        break
    a.append(m)
print(index)
