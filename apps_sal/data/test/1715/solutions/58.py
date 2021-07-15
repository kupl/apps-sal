a,b,q = map(int, input().split())

s = [int(input()) for i in range(a)]
t = [int(input()) for i in range(b)]

import bisect

for i in range(q):
    s2 = 10**12
    t2 = 10**12
    qq = int(input())
    sp = bisect.bisect(s,qq)
    tp = bisect.bisect(t,qq)
    s1 = s[sp-1]
    if sp <a:
        s2 = s[sp]

    t1 = t[tp-1]
    if tp <b:
        t2 = t[tp]
    print(min(abs(qq-s1)+abs(s1-t1),abs(qq-s1)+abs(s1-t2),
              abs(qq-s2)+abs(s2-t1),abs(qq-s2)+abs(s2-t2),
              abs(qq-t1)+abs(t1-s1),abs(qq-t1)+abs(t1-s2),
              abs(qq-t2)+abs(t2-s1),abs(qq-t2)+abs(t2-s2)))
