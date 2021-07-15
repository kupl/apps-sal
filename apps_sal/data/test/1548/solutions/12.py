from collections import deque
n = int(input())

sticks = list(map(int, input().split()))
dq = deque(sorted(sticks))

lenx=0
leny=0
while len(dq) > 0:
    lenx+=dq.pop()
    if len(dq)>0:
        leny+=dq.popleft()
print(lenx**2+leny**2)



