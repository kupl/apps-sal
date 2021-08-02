n, m, k = list(map(int, input().split()))
h = {int(x) for x in input().split()}
p = 1
for t in range(k):
    u, v = list(map(int, input().split()))
    if p in h:
        break
    elif p == u:
        p = v
    elif p == v:
        p = u

print(p)
