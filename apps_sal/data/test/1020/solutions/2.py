N, W, k = map(int, input().split())
res = 0
for i in range(k):
    res += (N + W) * 2 - 4
    N -= 4
    W -= 4
print(res)
