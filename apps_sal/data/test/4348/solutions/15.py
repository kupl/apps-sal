(n, k) = list(map(int, input().split()))
s = list(input())
cnt = {}
d = {}
for (i, c) in enumerate(s):
    if c not in cnt:
        cnt[c] = 1
        d[c] = [i]
    else:
        cnt[c] += 1
        d[c].append(i)
ch = ''
for c in sorted(cnt):
    if k - cnt[c] <= 0:
        ch = c
        break
    for i in d[c]:
        s[i] = ''
    k -= cnt[c]
for i in d[ch][:k]:
    s[i] = ''
print(''.join(s))
