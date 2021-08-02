import sys
from collections import deque
input = sys.stdin.readline


q = int(input())
s = [input() for i in range(q)]
for i in range(q):
    a0 = deque([])
    a1 = deque([])
    for j in range(len(s[i]) - 1):
        tmp = int(s[i][j])
        if tmp % 2 == 0:
            a0.append(tmp)
        else:
            a1.append(tmp)
    ans = []
    while True:
        if a0 and a1:
            if a0[0] > a1[0]:
                tmp = a1.popleft()
                ans.append(tmp)
            else:
                tmp = a0.popleft()
                ans.append(tmp)
        else:
            while a0:
                tmp = a0.popleft()
                ans.append(tmp)
            while a1:
                tmp = a1.popleft()
                ans.append(tmp)
            break
    print("".join(map(str, ans)))
