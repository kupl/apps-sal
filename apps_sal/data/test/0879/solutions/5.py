from collections import deque
n = int(input())
a = list(map(int, input().split()))
k = a[-1]
answ = deque()
answ.appendleft(n)
while k != 1:
    answ.appendleft(k)
    k = a[k - 2]
answ.appendleft(k)
print(' '.join((str(x) for x in answ)))
