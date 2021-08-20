BIT = [0] * 10 ** 6


def update(idx):
    while idx < len(BIT):
        BIT[idx] += 1
        idx += idx & -idx


def query(idx):
    s = 0
    while idx > 0:
        s += BIT[idx]
        idx -= idx & -idx
    return s


n = int(input())
a = list(map(int, input().split()))
ans = 0
cnt = {}
l = [0] * n
r = [0] * n
for i in range(n):
    cnt[a[i]] = cnt.get(a[i], 0) + 1
    l[i] = cnt[a[i]]
cnt.clear()
for i in range(n - 1, -1, -1):
    cnt[a[i]] = cnt.get(a[i], 0) + 1
    r[i] = cnt[a[i]]
    if i < n - 1:
        ans += query(l[i] - 1)
    update(r[i])
print(ans)
