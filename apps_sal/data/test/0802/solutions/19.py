(n, s) = (int(input()), input())
dis = len(set(s))
mp = {}
(l, r, m, cnt) = (0, 0, 99999999, 0)
for c in s:
    if c not in mp:
        mp[c] = 0
        cnt += 1
    mp[c] += 1
    if cnt == dis:
        while mp[s[l]] > 1:
            mp[s[l]] -= 1
            l += 1
        m = min(m, r - l + 1)
    r += 1
print(m)
