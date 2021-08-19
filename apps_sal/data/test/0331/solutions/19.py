(n, m, k) = map(int, input().split())
data = map(int, input().split())
temp = [abs(m - 1 - i) for (i, v) in enumerate(data) if v and v <= k]
res = min(temp)
print(res * 10)
