def f():
    return [*map(int, input().split())]


(k, n) = f()
l = f()
l += [l[0] + k]
a = 0
for i in range(n):
    a = max(a, l[i + 1] - l[i])
print(k - a)
