(n, k) = list(map(int, input().split()))
b = list(map(int, input().split()))
d = [0 for i in range(100)]
for i in b:
    d[i - 1] += 1
if max(d) % k == 0:
    m = max(d)
else:
    m = max(d) + (k - max(d) % k)
s = 0
for i in d:
    if i != 0:
        s += m - i
print(s)
