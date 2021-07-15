import collections

n, q = list(map(int, input().split()))
d = collections.defaultdict(list)
cnt, t = [0] * 6, [0] * 6
for i in range(q):
    s1, s2 = input().split()
    d[s2].append(s1)
    cnt[ord(s2) - ord('a')] += 1
for s in d['a']:
    t[ord(s[0]) - ord('a')] += 1
for i in range(n - 2):
    p = [0] * 6
    for j in range(6):
        if t[j] == 0:
            continue
        for s in d[chr(j + 97)]:
            p[ord(s[0]) - ord('a')] += t[j]
    t = p
print(sum(t))
    

