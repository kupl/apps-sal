n = int(input())
r = [[]for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    r[u].append(v)
    r[v].append(u)

if n == 1:
    print(0)
else:
    st = [(0, 0, 1 / len(r[0]))]
    ans = 0
    rsum = 0
    visit = [False] * n
    visit[0] = True
    while st:
        v, t, m = st.pop()
        for l in r[v]:
            if not visit[l]:
                if l != 0 and len(r[l]) == 1:
                    ans += (t + 1) * m
                    rsum += 1
                else:
                    st.append((l, t + 1, m / (len(r[l]) - 1)))
                visit[l] = True
    print(ans)
