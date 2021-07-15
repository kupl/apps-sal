R = lambda: map(int, input().split())

n, k = R()
a = list(R())
b = sorted(a)
b = b[n-k:]
ans = []

print(sum(b))

k = 0
for t in a:
    k += 1
    if t in b:
        del b[b.index(t)]
        ans.append(k)
        k = 0
if k:
    ans[-1] += k

print(*ans, sep=' ')
