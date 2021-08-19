from collections import defaultdict
(n, m) = map(int, input().split())
A = list(map(int, input().split()))
dic = defaultdict(int)
dic[0] += 1
cum = 0
for i in range(n):
    cum += A[i]
    dic[cum % m] += 1
ans = 0
for v in dic.values():
    ans += v * (v - 1) // 2
print(ans)
