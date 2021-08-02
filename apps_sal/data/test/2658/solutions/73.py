from collections import deque
import sys
n, k = map(int, input().split())
A = list(map(int, input().split()))
A = list(map(lambda x: x - 1, A))
seen = [0] * n
li = deque()
pos = 0
while True:
    if seen[pos]:
        while li[0] != pos:
            li.popleft()
            k -= 1
            if k == 0:
                print(li[0] + 1)
                return
        break
    li.append(pos)
    seen[pos] = 1
    pos = A[pos]

print(li[k % len(li)] + 1)
