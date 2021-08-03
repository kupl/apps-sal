from collections import Counter

n = int(input())
d = Counter(list(map(int, input().split())))

ans = 0
for k, v in d.items():
    if k > v:
        ans += v
    elif k < v:
        ans += v - k
print(ans)
