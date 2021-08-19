# -*- coding: utf-8 -*-
"""
yl3 jeopardy
"""
def a(): return list(map(int, input().split()))


n, m = a()
sa = a()
sb = a()
au = []

for i in reversed(sorted(sb)):
    au.append(sa.pop(i - 1))
su = sum(sa)
au.sort(reverse=True)
for i in range(m):
    t = au.pop(0)
    if t > su:
        su += t
    else:
        su *= 2
print(su)
