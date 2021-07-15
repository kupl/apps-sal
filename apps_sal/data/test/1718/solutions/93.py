# 34
N, K = map(int, input().split())
a = list(map(int, input().split()))

mn = min(a)
count_mn = a.count(mn)
ans = 0
for i in range(count_mn):
    N -= K
    ans += 1
    if N < 0: break
K -= 1
if N > 0:
    ans += N // K if N % K == 0 else N // K + 1
print(ans)
