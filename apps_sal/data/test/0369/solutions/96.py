import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import deque

n, m = list(map(int, readline().split()))
s = readline().rstrip().decode()[::-1]
index = 0
ans = deque([])
for i in range(n):
    for j in range(m, 0, -1):
        if index + j >= n:
            ans.appendleft(n - index)
            print((*ans))
            return
        if s[index + j] == '0':
            ans.appendleft(j)
            index += j
            break
    else:
        print((-1))
        return

