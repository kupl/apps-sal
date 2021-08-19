from collections import Counter
n = int(input())
A = list(map(int, input().split()))
cnt_A = Counter(A)
ans = 0
for (k, v) in cnt_A.items():
    if v - k >= 0:
        ans += v - k
    else:
        ans += v
print(ans)
