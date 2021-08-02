from collections import deque

N, M = list(map(int, input().split()))

a = deque()
b = deque()
for i in range(1, int(M ** (1 / 2)) + 1):
    if M % i == 0:
        a.appendleft(i)
        b.append(M // i)

b.extend(a)

for i in b:
    m = M // i
    if m >= N:
        print(i)
        break
