n, k = map(int, input().split())
p = [(int(i) + 1) / 2 for i in input().split()]
res = [sum(p[:k])]
for i in range(n-k): res.append(res[i] - p[i] + p[i+k])
print(max(res))
