from collections import deque

n, m, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a = sorted(a)
a = deque(a)
first = - 10e7
r = deque([])
s = 0
result = 0
while n > 0:
    e = a[0]
    c = e - m + 1
    while r != deque([]):
        if r[0] < c:
            r.popleft()
            s -= 1
        else:
            break
    if s + 1 >= k:
        result += 1
    else:
        r.append(e)
        s += 1
    a.popleft()
    n -= 1
    # print(e, c, s, r, result)

print(result)
