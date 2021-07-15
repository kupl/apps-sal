# -*- coding: utf-8 -*-

s = list(input())
t = list(input())

N = len(s)
M = len(t)

s_d = sorted(s)
t_d = sorted(t, reverse=True)

ans ='No'
if N < M:
    new_t = "".join(t_d[:N])
    new_s = "".join(s_d)
    if new_t == new_s:
        ans ='Yes'

if ans == 'No':
    pos = 0
    for i in range(min(N, M)):
        if s_d[i]!=t_d[i]:
            pos = i
            break
    if s_d[pos] < t_d[pos]:
        ans ='Yes'

print(ans)
