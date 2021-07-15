from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

b = []
for x in a:
    if not b or b[-1] != x:
        b.append(x)
p = defaultdict(list)
for i in range(len(b)):
    p[b[i]].append(i)

ans = cur = 0
for r in range(1, n + 1):
    for i in p[r]:
        cur += r
        if len(b) == 1:
            pass
        elif i == 0:
            if b[i + 1] < b[i]:
                cur -= b[i + 1]
        elif i == len(b) - 1:
            if b[i - 1] < b[i]:
                cur -= b[i - 1]
        else:
            mx = max(b[i - 1], b[i + 1])
            mn = min(b[i - 1], b[i + 1])
            if mx < b[i]:
                cur -= mx + mn
            elif mn < b[i]:
                cur -= mn
    ans += cur
print(ans)
