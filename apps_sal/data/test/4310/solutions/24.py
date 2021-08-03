L = list(map(int, input().split()))
L.sort()
a = 0
for i in range(len(L) - 1):
    a = L[i + 1] - L[i] + a
print(a)
