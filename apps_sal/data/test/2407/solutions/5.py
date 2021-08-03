import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    n, r = list(map(int, input()[:-1].split()))
    arr = list(sorted(list(map(int, input()[:-1].split()))))
    deq = deque(arr)

    ans = 0
    rnow = 0

    while len(deq) > 0:
        x = deq.pop()
        while len(deq) > 0 and deq[-1] == x:
            deq.pop()
        rnow += r
        while len(deq) > 0 and deq[0] <= rnow:
            deq.popleft()
        ans += 1
    print(ans)
