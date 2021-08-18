import sys
sys.setrecursionlimit(100000)


N, K = list(map(int, input().split()))

tree = [[] for _ in range(N + 10)]

for i in range(N - 1):
    a, b = list(map(int, input().split()))
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)

ans = []


def wfs(now, back):
    if now != 0:
        cnt = K - 2
    else:
        cnt = K - 1
    for nxt in tree[now]:
        if nxt != back:
            ans.append(cnt)
            cnt = cnt - 1
            wfs(nxt, now)


ans.append(K)
wfs(0, -1)

ans2 = 1
for j in range(len(ans)):
    ans2 = (ans2 * ans[j]) % (10**9 + 7)
print(ans2)
