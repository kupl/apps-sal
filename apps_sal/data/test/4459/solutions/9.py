from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
hashmap = defaultdict(int)
for a in A:
    hashmap[a] += 1
ans = 0
for k, v in hashmap.items():
    if k < v:
        ans += v - k
    elif k > v:
        ans += v
print(ans)
