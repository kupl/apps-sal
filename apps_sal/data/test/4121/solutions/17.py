import sys


def rint():
    return map(int, sys.stdin.readline().split())


h = 0
l = 1
n = int(input())

a = rint()

a = [i % 2 for i in a]

cnt = 0
cur = -1
ae = []
for i in range(n):
    if a[i] == 0:
        if cur == 0 or cur == -1:
            cur = 0
            cnt += 1
        else:
            ae.append([cur, cnt % 2])
            cnt = 1
            cur = 0
    else:
        if cur == 1 or cur == -1:
            cur = 1
            cnt += 1
        else:
            ae.append([cur, cnt % 2])
            cnt = 1
            cur = 1
ae.append([cur, cnt % 2])
stack = []
for e in ae:
    if e[l] == 1:
        if len(stack) == 0:
            stack.append(e[h])
        else:
            if e[h] == stack[-1]:
                stack.pop()
            else:
                stack.append(e[h])
if len(stack) > 1:
    print("NO")
else:
    print("YES")
