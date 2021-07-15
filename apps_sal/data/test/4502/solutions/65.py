from collections import deque

n = int(input())
a_s = list(map(int, input().split()))

d = deque()

for i in range(n):
    if i % 2 == 0:
        d.append(a_s[i])
    else:
        d.appendleft(a_s[i])

if n%2==1:
    d.reverse()

print((' '.join(map(str, d))))

