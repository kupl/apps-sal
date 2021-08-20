n = int(input())
a = [0] + list(map(int, input().split()))
d = {}
b = []
for i in range(1, n + 1):
    d[a[i]] = i
m = 0
for i in range(1, n + 1):
    ele = a[i]
    if ele != i and abs(i - d[i]) * 2 >= n:
        m += 1
        b.append([i, d[i]])
        a[i] = i
        a[d[i]] = ele
        d[ele] = d[i]
        d[i] = i
    elif ele != i and abs(i - d[i]) * 2 < n and (i <= n // 2) and (2 * (d[i] - 1) >= n):
        m += 5
        b.append([1, d[i]])
        b.append([1, n])
        b.append([i, n])
        b.append([1, n])
        b.append([1, d[i]])
        a[i] = i
        a[d[i]] = ele
        d[ele] = d[i]
        d[i] = i
    elif ele != i and abs(i - d[i]) * 2 < n and (i <= n // 2) and (2 * (d[i] - 1) < n):
        m += 3
        b.append([n, d[i]])
        b.append([i, n])
        b.append([n, d[i]])
        a[i] = i
        a[d[i]] = ele
        d[ele] = d[i]
        d[i] = i
    elif ele != i and abs(i - d[i]) * 2 < n:
        m += 3
        b.append([1, d[i]])
        b.append([i, 1])
        b.append([1, d[i]])
        a[i] = i
        a[d[i]] = ele
        d[ele] = d[i]
        d[i] = i
print(m)
for i in b:
    print(*i)
