from collections import Counter

n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
CA = Counter(A)

kouho = CA.most_common()[::-1]
ans = 0
idx = 0
while idx < len(CA) - k:
    key, val = kouho[idx]
    ans += val
    idx += 1
print(ans)
