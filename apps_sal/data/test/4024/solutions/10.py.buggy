from collections import deque
n, m = list(map(int, input().split()))
s = input()
d = deque([s])
ans = 1
an = 0
dd = {}
while d and ans < m:
    # print(d)
    p = d.popleft()
    dd[p] = 1
    k = len(p)
    for i in range(k):
        pp = p[:i] + p[i + 1:]
        # print(pp,dd)
        if (pp not in dd):
            an += (n - (k - 1))
            ans += 1
            dd[pp] = 1
            d.append(pp)
        if ans == m:
            print(an)
            return

    # print(d)
# print(an,ans)
if ans == m:
    print(an)
else:
    print(-1)
