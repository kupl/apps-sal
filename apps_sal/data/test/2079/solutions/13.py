from collections import deque
n = int(input())
w = list(map(int, input().split()))
w = sorted(range(len(w)), key=w.__getitem__)
w = iter(w)
e = list(input())
s = deque()
for e1 in e:
    if e1 == '0':
        x = next(w) + 1
        print(x, end=' ')
        s.append(x)
    else:
        print(s.pop(), end=' ')
