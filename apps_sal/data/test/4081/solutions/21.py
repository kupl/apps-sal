from collections import deque
n = int(input())
a = list(map(int, input().split()))
a = deque(a)
p = 0
b = []
for i in range(n):
    if a[0] >= a[-1] and a[-1] > p:
        p = a.pop()
        b.append('R')
    elif a[0] >= a[-1] and a[0] > p:
        p = a.popleft()
        b.append('L')
    elif a[-1] >= a[0] and a[0] > p:
        p = a.popleft()
        b.append('L')
    elif a[-1] >= a[0] and a[-1] > p:
        p = a.pop()
        b.append('R')
    else:
        break
print(len(b))
print(''.join(b))
