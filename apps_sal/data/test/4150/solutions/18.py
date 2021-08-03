n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
pos = {}
pre = [i - 1 for i in range(n + 2)]
nex = [i + 1 for i in range(n + 2)]
for i, j in enumerate(a):
    pos[j] = i + 1
group = 1
taken = [0 for _ in range(n + 2)]
right = left = 0
for i in range(n, 0, -1):
    if taken[pos[i]] != 0:
        continue
    group = (group + 1) % 2
    p = k
    now = pos[i]
    taken[now] = group + 1
    while p > 0 and now <= n:
        now = nex[now]
        if taken[now] == 0:
            taken[now] = group + 1
            p -= 1
        right = now
    p = k
    now = pos[i]
    while p > 0 and now > 0:
        now = pre[now]
        if taken[now] == 0:
            taken[now] = group + 1
            p -= 1
        left = now
    nex[left] = right
    pre[right] = left
ans = [str(i) for i in taken]
print(''.join(ans[1:n + 1]))
