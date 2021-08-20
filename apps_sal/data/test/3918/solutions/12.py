(n, k1, k2) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
k = k1 + k2
d = [abs(a[i] - b[i]) for i in range(n)]
if sum(d) > k:
    for i in range(k):
        m = max(d)
        d.remove(m)
        d.append(m - 1)
    ans = sum((x ** 2 for x in d))
    print(ans)
else:
    print((k - sum(d)) % 2)
