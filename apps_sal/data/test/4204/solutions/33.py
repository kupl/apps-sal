S = list(map(int, input()))
K = int(input())

res = []
for c in S:
    res.append(c)
    if c != 1:
        break
print((res[min(len(res) - 1, K - 1)]))
