def f():
    return map(int, input().split())


(n, k) = f()
d = n - k
s = d >> 1
y = sum((q & 1 for q in f()))
x = n - y
t = s < y and (k & 1 or s < x) if d & 1 else k & 1 and s >= x if d else y & 1
print(['Daenerys', 'Stannis'][t])
