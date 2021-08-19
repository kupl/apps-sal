from collections import deque
(n, m) = map(int, input().split())
x = deque(range(1, n + 1))
aaa = []
bbb = []
flag = True
if n % 2 == 1:
    for i in range(m):
        a = x.popleft()
        aaa.append(a)
        b = x.pop()
        bbb.append(b)
else:
    for i in range(m):
        a = x.popleft()
        aaa.append(a)
        b = x.pop()
        bbb.append(b)
        if x[-1] - x[0] <= n // 2 and flag:
            a = x.popleft()
            flag = False
for (aa, bb) in zip(aaa, bbb):
    print(aa, bb)
