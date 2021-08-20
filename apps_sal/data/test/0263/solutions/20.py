n = int(input().rstrip())
m = int(input().rstrip())
L = []
for _ in range(n):
    a = int(input().rstrip())
    L.append(a)
max_a = m + max(L)
k = m
while k:
    L[L.index(min(L))] = min(L) + 1
    k = k - 1
min_a = max(L)
print(str(min_a) + ' ' + str(max_a))
