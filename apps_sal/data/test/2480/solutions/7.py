n, k = list(map(int, input().split()))
l = list(map(int, input().split()))
mo = [0]
mod = [0]
for i in range(n):
    a = l[i] % k
    mo.append((a + mo[-1]) % k)
    mod.append((mo[-1] - (i + 1)) % k)
dic = {0: 1}
le = 1
ans = 0
for i in range(1, n + 1):
    if le < k:
        if mod[i] in dic:
            ans += dic[mod[i]]
            dic[mod[i]] += 1
        else:
            dic[mod[i]] = 1
        le += 1
    else:
        dic[mod[i - k]] -= 1
        if mod[i] in dic:
            ans += dic[mod[i]]
            dic[mod[i]] += 1
        else:
            dic[mod[i]] = 1

print(ans)
