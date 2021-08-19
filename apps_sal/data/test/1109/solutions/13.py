def read():
    return list(map(int, input().split()))


(n, k) = read()
m = n // k
a = list(read())
result = 0
for i in range(k):
    t = a[i:n:k]
    s = t.count(1)
    result += min(s, m - s)
print(result)
