from collections import deque
from itertools import accumulate
(n, m, k) = map(int, input().split())
a_list = list(accumulate(list(map(int, input().split()))))
a_list = [0] + a_list
b_list = list(accumulate(list(map(int, input().split()))))
b_list = [0] + b_list + [float('inf')]
cnt_list = []
for i in range(len(a_list)):
    t = k
    cnt = 0
    a = a_list[i]
    if t < a:
        continue
    t -= a
    cnt += i
    ok = 0
    no = m + 2
    while no != ok + 1:
        center = (ok + no) // 2
        if t >= b_list[center]:
            ok = center
        if t < b_list[center]:
            no = center
    cnt += ok
    cnt_list.append(cnt)
ans = max(cnt_list)
print(ans)
