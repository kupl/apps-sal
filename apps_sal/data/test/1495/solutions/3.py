def read(): return list(map(int, input().split()))


n = int(input())
a = list(read())
m = max(a) + 5
cnt = [0] * m
step = [0] * m
was = [-1] * m
for i in range(n):
    x = a[i]
    q = [(x, 0)]
    st = 0
    while st < len(q):
        x, y = q[st]
        st += 1
        if x >= m or was[x] == i:
            continue
        was[x] = i
        step[x] += y
        cnt[x] += 1
        q.append((x * 2, y + 1))
        q.append((x // 2, y + 1))
ans = min(step[x] for x in range(m) if cnt[x] == n)
print(ans)
