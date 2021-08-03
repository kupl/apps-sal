n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

cnt = [0 for _ in range(101)]
for ai in a:
    cnt[ai] += 1
l = 0
r = 101
while l + 1 < r:
    c = (l + r) // 2
    k = 0
    for i in range(1, 101):
        k += cnt[i] // c
    if n <= k:
        l = c
    else:
        r = c
print(l)
