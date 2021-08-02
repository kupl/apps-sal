k = 0
i = 0
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for j in a:
    if m > 1:
        while (j > b[i + 1] and i + 2 < m):
            i += 1
        w = abs(b[i] - j)
        e = abs(b[i + 1] - j)
        k1 = min(w, e)
        k = max(k, k1)
    else:
        k = max(k, abs(b[0] - j))
print(k)
