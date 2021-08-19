from collections import defaultdict
(n, k) = list(map(int, input().split()))
l = list(map(int, input().split()))
mod = [0]
for i in range(n):
    a = (l[i] - 1) % k
    mod.append((mod[-1] + a) % k)
dic = {0: 1}
ans = 0
for i in range(1, n + 1):
    if i < k:
        if mod[i] in dic:
            ans += dic[mod[i]]
            dic[mod[i]] += 1
        else:
            dic[mod[i]] = 1
    else:
        dic[mod[i - k]] -= 1
        if mod[i] in dic:
            ans += dic[mod[i]]
            dic[mod[i]] += 1
        else:
            dic[mod[i]] = 1
print(ans)
