from collections import Counter
n = int(input())
aa = Counter(map(int, input().split()))
ans = 0
for (k, v) in aa.items():
    if k < v:
        ans += v - k
    elif k > v:
        ans += v
print(ans)
