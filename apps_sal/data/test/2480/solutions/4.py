from collections import defaultdict
(n, k) = list(map(int, input().split()))
A = list(map(int, input().split()))
accm = [0] * (n + 1)
for i in range(n):
    accm[i + 1] = accm[i] + A[i]
li = [(val - itr) % k for (itr, val) in enumerate(accm)]
ans = 0
box = defaultdict(int)
for i in range(n + 1):
    if i >= k:
        box[li[i - k]] -= 1
    ans += box[li[i]]
    box[li[i]] += 1
print(ans)
