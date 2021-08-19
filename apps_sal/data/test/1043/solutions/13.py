import heapq
pop = heapq.heappop
push = heapq.heappush
n = int(input())
a = list(map(int, input().split()))
ans = 0
pos = -1
for (i, x) in enumerate(a):
    if x == -1:
        pos = i
        break
if pos == n - 1:
    print(0)
else:
    ans += a[n - 1]
    cur = n - 2
    used = [0] * n
    used[pos] = 1
    used[n - 1] = 1
    Q = []
    i = n // 2
    while i >= 2:
        for _ in range(i):
            while used[cur] == 1:
                cur -= 1
            val = 0 if cur < pos else a[cur]
            push(Q, (val, cur))
            cur -= 1
        while True:
            (x, p) = pop(Q)
            if used[p] == 0:
                break
        used[p] = 1
        if p > pos:
            ans += a[p]
        i //= 2
    print(ans)
