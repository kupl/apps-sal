from collections import deque

K = int(input())

visited=[False]*K
s=(1,1)

q = deque()
q.append(s)

while True:
  c = q.popleft()
  visited[c[0]] = True

  if c[0] == 0:
    print(c[1])
    return

  if not visited[(c[0] * 10) % K] and not visited[(c[0] * 10) % K]:
    q.appendleft(((c[0] * 10) % K, c[1]))

  if not visited[(c[0] + 1) % K] and not visited[(c[0] + 1) % K]:
    q.append(((c[0] + 1) % K, c[1] + 1))
