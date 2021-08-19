import sys
from collections import deque
# sys.stdin = open("ivo.in")

n, m = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))

b = []
mx = 0
for i in range(m):
    t = tuple(map(int, sys.stdin.readline().split()))
    mx = max([mx, t[1]])
    b.append(t)

real = []
so_far = 0
for i in range(m - 1, -1, -1):
    if b[i][1] > so_far:
        real.append(b[i])
        so_far = b[i][1]

real.reverse()

answer = [0] * n
b = a[0:mx]
b.sort()
d = deque(b)

for i in range(mx, len(a)):
    answer[i] = a[i]

for i in range(len(real)):
    if i + 1 == len(real):
        for j in range(real[i][1]):
            if real[i][0] == 1:
                answer[j] = d.popleft()
            else:
                answer[j] = d.pop()
    else:
        for j in range(real[i][1] - 1, real[i + 1][1] - 1, -1):
            if real[i][0] == 1:
                answer[j] = d.pop()
            else:
                answer[j] = d.popleft()

print(" ".join(map(str, answer)))
