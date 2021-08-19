import collections
(n, s) = map(str, input().split())
ans = 0
for i in range(int(n)):
    cnt = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    cnt[s[i]] += 1
    for j in range(i + 1, int(n)):
        cnt[s[j]] += 1
        if cnt['A'] == cnt['T'] and cnt['C'] == cnt['G']:
            ans += 1
print(ans)
