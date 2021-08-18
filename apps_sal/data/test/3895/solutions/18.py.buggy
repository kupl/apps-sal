n = int(input())
f = list(map(int, input().split()))
h = {}
g = []
for i in f:
    if f[i - 1] != i:
        print(-1)
        return
    elif i not in h:
        h[i] = len(g)
        g.append(i)
print(len(g))
for i in f:
    print(h[i] + 1, end=' ')
print()
print(*g)
