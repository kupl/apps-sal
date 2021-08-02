n, m = map(int, input().split())
l = [int(x) for x in input().split()]
pairs = [[] for i in range(n + 1)]
ans = 0
N = [0 for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    pairs[b].append(a)
for i in range(n - 1, -1, -1):
    if N[l[i]] == n - 1 - i - ans and i != n - 1:
        ans += 1
    else:
        for I in pairs[l[i]]:
            N[I] += 1
print(ans)
