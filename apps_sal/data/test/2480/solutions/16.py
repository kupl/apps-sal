from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    a[i] -= 1
    a[i] %= k

S = [0]
for i in range(n):
    S.append((S[-1] + a[i]) % k)

ans = 0
dic = defaultdict(int)
dic[0] = 1
for i in range(1, n + 1):
    if i >= k:
        dic[S[i - k]] -= 1
    ans += max(0, dic[S[i]])
    dic[(S[i])] += 1

print(ans)
