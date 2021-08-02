from collections import deque

K = int(input())
q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

for i in range(K):
    runrun = q.popleft()
    rem = runrun % 10
    if rem == 0:
        q.append(runrun * 10)
        q.append(runrun * 10 + rem + 1)
    elif rem == 9:
        q.append(runrun * 10 + rem - 1)
        q.append(runrun * 10 + rem)
    else:
        q.append(runrun * 10 + rem - 1)
        q.append(runrun * 10 + rem)
        q.append(runrun * 10 + rem + 1)

print(runrun)
