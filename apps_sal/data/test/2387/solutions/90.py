import bisect

n = int(input())
opens = 0
closes = 0
ls = []
rs = []
for _ in range(n):
    s = input()
    cnt1 = 0
    cnt2 = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt1 += 1
        else:
            if cnt1 == 0:
                cnt2 += 1
            else:
                cnt1 -= 1
    if cnt2 == 0:
        opens += cnt1
    elif cnt1 == 0:
        closes += cnt2
    else:
        ls.append(cnt2)
        rs.append(cnt1)
ls = sorted(ls)
rs = sorted(rs)
lefts = sum(ls)
rights = sum(rs)
if opens - closes != lefts - rights:
    print('No')
else:
    flag = False
    if len(ls) == 0:
        flag = True
    for a in ls:
        if opens < a or closes < a + (rights - lefts):
            continue
        pos = bisect.bisect_right(rs, a + (rights - lefts))
        if pos != 0:
            flag = True
            break
    for b in rs:
        if opens < b + (lefts - rights) or closes < b:
            continue
        pos = bisect.bisect_right(ls, b + (lefts - rights))
        if pos != 0:
            flag = True
            break
    if flag == True:
        print('Yes')
    else:
        print('No')
