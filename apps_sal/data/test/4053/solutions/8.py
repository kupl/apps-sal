import sys
from math import floor, ceil

input = sys.stdin.readline

n = int(input())

q = {}
for i in range(2 * n - 2):
    curr = input().strip()
    if len(curr) not in q.keys():
        q[len(curr)] = []
    q[len(curr)].append((curr, i))

pre = q[1][0][0]
suf = q[1][1][0]
ans = [0 for i in range(2 * n - 2)]
ans[q[1][0][1]] = 'P'
ans[q[1][1][1]] = 'S'

valid = True
for i in range(2, n):
    first = q[i][0]
    second = q[i][1]
    # assuming first is prefix and second is suffix
    if (first[0][:-1] == pre) and (second[0][1:] == suf):
        ans[first[1]] = 'P'
        ans[second[1]] = 'S'
        pre = first[0]
        suf = second[0]
    elif (first[0][1:] == suf) and (second[0][:-1] == pre):
        ans[first[1]] = 'S'
        ans[second[1]] = 'P'
        suf = first[0]
        pre = second[0]
    else:
        valid = False
        break

if not valid:
    pre = q[1][1][0]
    suf = q[1][0][0]
    ans = [0 for i in range(2 * n - 2)]
    ans[q[1][0][1]] = 'S'
    ans[q[1][1][1]] = 'P'

    valid = True
    for i in range(2, n):
        first = q[i][0]
        second = q[i][1]
        # assuming first is prefix and second is suffix
        if (first[0][:-1] == pre) and (second[0][1:] == suf):
            ans[first[1]] = 'P'
            ans[second[1]] = 'S'
            pre = first[0]
            suf = second[0]
        elif (first[0][1:] == suf) and (second[0][:-1] == pre):
            ans[first[1]] = 'S'
            ans[second[1]] = 'P'
            suf = first[0]
            pre = second[0]
        else:
            valid = False
            break
print(''.join([str(x) for x in ans]))
