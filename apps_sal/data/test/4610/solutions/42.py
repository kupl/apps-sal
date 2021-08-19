from collections import Counter
(n, k) = map(int, input().split())
a = list(map(int, input().split()))
l = Counter(a)
if len(set(a)) <= k:
    print(0)
else:
    ci = list(l.values())
    ci.sort()
    i = 0
    cnt = len(ci)
    ans = 0
    while cnt > k:
        cnt -= 1
        ans += ci[i]
        i += 1
    print(ans)
