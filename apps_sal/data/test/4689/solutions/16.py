k, n = map(int, input().split())
L = list(map(int, input().split()))
L.append(k + L[0])
m = 0

for i in range(n):
    m = max(m, L[i + 1] - L[i])

print(k - m)
