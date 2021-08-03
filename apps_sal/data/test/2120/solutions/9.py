n, m = list(map(int, input().split()))
cs = [0] + list(map(int, input().split()))
mls = [0 for i in range(n + 1)]
for i in range(m):
    x, y = list(map(int, input().split()))
    if cs[y] < cs[x]:
        x, y = y, x
    mls[x] += 1
print(sum([cs[i] * mls[i] for i in range(n + 1)]))
