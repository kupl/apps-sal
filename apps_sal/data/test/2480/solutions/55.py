n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr = [i - 1 for i in arr]
acum = [0]
for i in range(n):
    acum.append(acum[-1] + arr[i])
acum = [i % k for i in acum]
ans = 0
dic = {}
for i in range(n + 1):
    if acum[i] % k not in dic:
        dic[acum[i]] = 1
    else:
        ans += dic[acum[i]]
        dic[acum[i]] += 1
    if i >= k - 1:
        dic[acum[i - k + 1]] -= 1
print(ans)
