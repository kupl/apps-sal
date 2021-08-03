n, k = list(map(int, input().split()))
L = list(map(int, input().split()))
L.sort()
s = 0
for i in range(n - k):
    s += L[i]

print((sum(L) - s))
