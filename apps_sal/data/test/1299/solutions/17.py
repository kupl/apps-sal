n, k = tuple(map(int, input().split(' ')))
ar = list(map(int, input().split(' ')))
t = [0]
for i in range(n):
    t.append(t[-1] + ar[i])
d = [0] * n
a = [0] * n
a1 = 0
b = k
m = 0
for i in range(k, n - k + 1):
    # print(a,b,d,m)
    if t[i] - t[i - k] > d[i - 1]:
        d[i] = t[i] - t[i - k]
        a[i] = i - k
    else:
        d[i] = d[i - 1]
        a[i] = a[i - 1]
    if d[i] + t[i + k] - t[i] > m:
        m = d[i] + t[i + k] - t[i]
        a1 = a[i]
        b = i
# print(a,b,d,m)
print('{0} {1}'.format(a1 + 1, b + 1))
