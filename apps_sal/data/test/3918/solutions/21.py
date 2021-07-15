n, k1, k2 = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = [abs(a[i]-b[i]) for i in range(n)]
k = k1 + k2
for _ in range(k):
    mx = max(d)
    id = d.index(mx)
    if mx == 0:
        d[id] += 1
    else:
        d[id] -= 1
print(sum([x ** 2 for x in d]))

