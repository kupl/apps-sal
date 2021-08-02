from collections import deque

__author__ = 'asmn'
n = int(input())

a = deque(map(int, input().split()))
s = [0, 0]
now = 0
while len(a) > 0:
    if a[0] > a[-1]:
        s[now] += a.popleft()
    else:
        s[now] += a.pop()
    now = 1 - now

print(s[0], s[1])
