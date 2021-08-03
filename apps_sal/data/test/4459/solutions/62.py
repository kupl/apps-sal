from collections import Counter
n = int(input())
a = list(map(int, input().split()))

count = Counter(a)
ans = 0
for k, v in count.items():
    if k < v:
        ans += v - k
    elif v < k:
        ans += v
print(ans)
