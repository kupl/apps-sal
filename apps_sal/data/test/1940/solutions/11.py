import math
(n, k) = list(map(int, input().split()))
w = [int(i) for i in input().split()]
res = []
for i in range(n):
    res.append(w[i] // k)
    res.append(bool(w[i] % k))
print(math.ceil(sum(res) / 2))
