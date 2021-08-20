import collections
n = int(input())
S = [input() for _ in range(n)]
cnt = collections.Counter(S[0])
for s in S[1:]:
    for a in cnt.keys():
        if a in s:
            cnt[a] = min(cnt[a], s.count(a))
        else:
            cnt[a] = 0
ans = [key * value for (key, value) in cnt.items() if value > 0]
ans = sorted(ans, reverse=False)
print(''.join(ans))
