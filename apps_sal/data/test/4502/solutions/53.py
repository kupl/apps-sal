from collections import deque


N = int(input())
AS = [int(i) for i in input().split()]

b = deque()

x = 0 if len(AS) % 2 == 0 else 1

for i, a in enumerate(AS):
  if i % 2 == x:
    b.append(str(a))
  else:
    b.appendleft(str(a))

print((' '.join(list(b))))

