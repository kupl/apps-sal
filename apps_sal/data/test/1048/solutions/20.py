n = int(input())
s = list(input())

d = 'UDLR'
cnt = {}
for c in d:
    cnt[c] = 0
for c in s:
    cnt[c] += 1
print(2 * (min(cnt['U'], cnt['D']) + min(cnt['L'], cnt['R'])))
