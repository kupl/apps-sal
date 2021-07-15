from collections import deque
from bisect import bisect_left, bisect_right

n, q = map(int, input().split())
list_x = deque()
list_y = deque()
memo_x = deque()
memo_y = deque()
x_now, y_now = n-1, n-1

ans = (n-2) ** 2

#que = [(1, i) for i in range(2, n)] + [(2, i) for i in range(2, n)]
for i in range(q):
    flg, x = map(int, input().split())
    if flg == 1:
        if x_now >= x:
            ans -= y_now - 1
            x_now = x - 1
            list_x.appendleft(x)
            memo_x.appendleft(y_now - 1)
        else:
            tmp = bisect_left(list_x, x) - 1
            ans -= memo_x[tmp]
    
    else:
        y = x
        if y_now >= y:
            ans -= x_now - 1
            y_now = y - 1
            list_y.appendleft(y)
            memo_y.appendleft(x_now - 1)
        else:
            tmp = bisect_left(list_y, y) - 1
            ans -= memo_y[tmp]

print(ans)
