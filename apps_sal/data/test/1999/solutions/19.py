n = int(input())
a = list(map(int, input().split()))
idx = {}
for i in range(n):
    x = a[i]
    while x in idx:
        del idx[x]
        x *= 2
    idx[x] = i
print(len(idx))
print(*list(idx.keys()))
