from collections import Counter
(n, k) = map(int, input().split())
s = list(map(int, input().split()))
num = Counter(s)
if len(num) <= k:
    print(0)
else:
    cnt = len(num) - k
    ans = 0
    i = 0
    for v in sorted(num.values()):
        if cnt == i:
            break
        ans += v
        i += 1
    print(ans)
