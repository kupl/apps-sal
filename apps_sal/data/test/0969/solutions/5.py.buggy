def find_max_substr(t, s):
    l, r = 0, len(t)
    while l != r:
        m = (l + r) // 2
        if t[:m + 1] in s:
            l = m + 1
        else:
            r = m
    l1 = l
    rs = s[::-1]
    l, r = 0, len(t)
    while l != r:
        m = (l + r) // 2
        if t[:m + 1] in rs:
            l = m + 1
        else:
            r = m
    l2 = l
    if l1 >= l2:
        return s.find(t[:l1]) + 1, s.find(t[:l1]) + l1
    else:
        return s.find(t[:l2][::-1]) + l2, s.find(t[:l2][::-1]) + 1


s = input()
t = input()
if not set(t).issubset(set(s)):
    print(-1)
    return
a = []
while t:
    l, r = find_max_substr(t, s)
    a.append((l, r))
    t = t[abs(r - l) + 1:]
print(len(a))
for l, r in a:
    print(l, r)
