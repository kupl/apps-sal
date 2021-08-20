def add(num):
    if num <= 1:
        return 0
    return num * (num - 1) // 2


(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
pre = [a[0]]
base = 2 ** k - 1
hb = 2 ** (k - 1)
for i in range(1, n):
    pre.append(a[i] ^ pre[-1])
cnt = dict()
cnt[0] = [0, 0]
for i in range(n):
    if pre[i] >= hb:
        if base - pre[i] not in cnt:
            cnt[base - pre[i]] = [0, 0]
        cnt[base - pre[i]][1] += 1
    else:
        if pre[i] not in cnt:
            cnt[pre[i]] = [0, 0]
        cnt[pre[i]][0] += 1
cnt1 = 0
for i in list(cnt.values()):
    sum1 = i[0] + i[1]
    cnt1 += add(sum1 // 2)
    cnt1 += add((sum1 + 1) // 2)
cnt1 += sum(cnt[0]) // 2
print(n * (n + 1) // 2 - cnt1)
