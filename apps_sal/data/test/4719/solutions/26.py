import collections
n = int(input())
s = list(input())
s_cnt = collections.Counter(s)
for i in range(n - 1):
    tmp = input()
    for k in s_cnt:
        s_cnt[k] = min(s_cnt[k], tmp.count(k))
s_cnt = dict(sorted(s_cnt.items(), key=lambda x: x[0]))
ans = ''
for k in s_cnt:
    ans += k * s_cnt[k]
print(ans)
