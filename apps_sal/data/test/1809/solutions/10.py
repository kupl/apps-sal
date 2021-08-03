n, m = map(int, input().split())
w = list(map(int, input().split()))
b = list(map(int, input().split()))
A = 0
for i in range(m):
    d, j = {}, i - 1
    while j >= 0 and b[j] != b[i]:
        if (d.get(b[j], 1)):
            A += w[b[j] - 1]
            d[b[j]] = 0
        j -= 1
print(A)
