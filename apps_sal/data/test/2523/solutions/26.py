s = input()
cs = []
cnt = 1
pre = s[0]
for si in s[1:]:
    if si == pre:
        cnt += 1
    else:
        cs.append(cnt)
        pre = si
        cnt = 1
cs.append(cnt)
n = len(s)
ans1 = n
merge = 0
no_merge = n
for i in range(len(cs)):
    merge += cs[i]
    no_merge -= cs[i]
    tmp = max(merge, no_merge)
    ans1 = min(ans1, tmp)
cs.reverse()
ans2 = n
merge = 0
no_merge = n
for i in range(len(cs)):
    merge += cs[i]
    no_merge -= cs[i]
    tmp = max(merge, no_merge)
    ans2 = min(ans2, tmp)
print((max(ans1, ans2)))
