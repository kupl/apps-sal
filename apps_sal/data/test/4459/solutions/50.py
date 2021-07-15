from collections import Counter

N, *A = list(map(int, open(0).read().split()))
cnt = Counter(A)
ans = 0
for k, v in list(cnt.items()):
    if k > v:
        ans += v
    else:
        ans += v - k
print(ans)

