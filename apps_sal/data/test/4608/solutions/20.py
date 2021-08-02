# -*- coding:utf-8 -*-

import sys
nyuryoku = [int(i) - 1 for i in sys.stdin]

N = nyuryoku[0] + 1
a_list = nyuryoku[1:]


cnt_push = 0
button_list = [False] * N
i = 0
#cur_but_posi = a_list[0]

while True:
    if button_list[i] == False:
        button_list[i] = True
        cnt_push += 1
        if a_list[i] == 1:
            break
        i = a_list[i]
    else:
        cnt_push = -1
        break

print(cnt_push)

"""
import sys

l = [int(i) - 1 for i in sys.stdin]

N = l[0] + 1

a = l[1:]

done = [False] * N

i = 0

ans = 0

while True:
    if done[i] == False:
        done[i] = True
        ans += 1
        if a[i] == 1:
            break
        i = a[i]
    else:
        ans = -1
        break

print(ans)
"""
