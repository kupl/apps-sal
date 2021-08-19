from collections import deque
import sys
n = int(input())
q = deque([])
toBe = 1
ans = 0
flag = 0
inp = [0] * (n * 2)
for i in range(2 * n):
    inp[i] = sys.stdin.readline().strip()
for i in range(2 * n):
    s = inp[i].split()
    if len(s) == 2:
        k = int(s[1])
        q.append(k)
        if len(q) == 1:
            continue
        if k != q[-2] - 1:
            flag = 0
    else:
        if q and toBe != q[-1]:
            flag = 1
            ans += 1
            q = []
        elif flag == 1:
            q = []
        else:
            q.pop()
        toBe += 1
sys.stdout.write(str(ans) + '\n')
