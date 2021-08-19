(n, k) = map(int, input().split())
a = list(map(int, input().split()))
s = [0]
for i in range(n):
    s.append((s[-1] + a[i] - 1) % k)
dic = {0: 1}
ans = 0
if n < k:
    for i in range(1, n + 1):
        if s[i] in dic:
            ans += dic[s[i]]
            dic[s[i]] += 1
        else:
            dic[s[i]] = 1
else:
    for i in range(1, k):
        if s[i] in dic:
            ans += dic[s[i]]
            dic[s[i]] += 1
        else:
            dic[s[i]] = 1
    for i in range(k, n + 1):
        dic[s[i - k]] -= 1
        if s[i] in dic:
            ans += dic[s[i]]
            dic[s[i]] += 1
        else:
            dic[s[i]] = 1
print(ans)
