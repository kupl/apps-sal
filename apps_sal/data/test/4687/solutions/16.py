from collections import defaultdict
(n, k) = map(int, input().split())
ans = 0
al = []
d = defaultdict(int)
for i in range(n):
    (a, b) = map(int, input().split())
    al.append(a)
    d[a] += b
al = list(set(al))
al.sort()
for i in al:
    if k > d[i]:
        k -= d[i]
    else:
        print(i)
        break
