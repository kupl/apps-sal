from collections import Counter

n, k = map(int, input().split())
A = list(map(int, input().split()))

cnt_A = sorted(Counter(A).values())

ans = 0
if len(cnt_A) <= k:
    print(ans)
else:
    for i in range(len(cnt_A) - k):
        ans += cnt_A[i]
    print(ans)
