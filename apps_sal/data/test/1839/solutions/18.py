n = int(input())
H = [False for i in range(n + 1)]
V = [False for i in range(n + 1)]
ans = []
for i in range(n ** 2):
    (h, v) = list(map(int, input().split()))
    if not H[h] and (not V[v]):
        H[h] = True
        V[v] = True
        ans.append(i + 1)
print(' '.join(map(str, ans)))
