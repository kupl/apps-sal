import itertools

n, m = map(int, input().split())
rin = [[]for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    rin[a - 1].append(b - 1)
    rin[b - 1].append(a - 1)

li = [i for i in range(2, n + 1)]

ans = 0

for v in itertools.permutations(li):
    pas = 0
    ch = 0
    st = 1
    for x in range(n - 1):
        if v[x] - 1 not in rin[st - 1]:
            ch += 1
            break
        else:
            st = v[x]
    if ch == 0:
        ans += 1

print(ans)
