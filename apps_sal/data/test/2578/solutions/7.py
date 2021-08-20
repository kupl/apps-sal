from sys import stdin
input = stdin.readline
(n, m) = map(int, input().split())
a = [[] for i in range(n)]
for i in range(m):
    b = list(map(int, input().split()))
    for j in range(2, b[0] + 1):
        a[b[j] - 1].append(b[j - 1] - 1)
        a[b[j - 1] - 1].append(b[j] - 1)
vis = [0] * n
ans = [0] * n
for i in range(n):
    if vis[i] == 0:
        st = [i]
        c = 0
        while st:
            x = st.pop()
            vis[x] = 1
            c += 1
            for j in a[x]:
                if vis[j] == 0:
                    vis[j] = 1
                    st.append(j)
        st = [i]
        ans[i] = c
        while st:
            x = st.pop()
            for j in a[x]:
                if ans[j] == 0:
                    ans[j] = c
                    st.append(j)
print(*ans)
