from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
counter = defaultdict(int)
ans = 0
for (i, v) in enumerate(a):
    ans += counter[i - v]
    counter[i + v] += 1
print(ans)
