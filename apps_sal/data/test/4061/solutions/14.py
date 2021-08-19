'''input
asdfasdf
fasd




'''
import sys
from collections import defaultdict as dd

mod = 10**9 + 7


def ri(flag=0):
    if flag == 0:
        return [int(i) for i in sys.stdin.readline().split()]
    else:
        return int(sys.stdin.readline())


st = input()
pat = input()
n = len(st)

forward = [0 for i in range(n)]

idx = 0

for i in range(n):
    if idx < len(pat) and st[i] == pat[idx]:
        idx += 1
        forward[i] = idx

backward = [0 for x in range(n)]

idx = len(pat) - 1

for i in range(n - 1, -1, -1):
    if idx >= 0 and st[i] == pat[idx]:
        idx -= 1
        backward[i] = idx + 2

# print(forward)
# print(backward)

c1 = dd(int)
c2 = dd(int)

for i in range(n):
    c1[forward[i]] = i + 1
    c2[backward[i]] = i + 1

ans = max(c2[1] - 1, n - c1[len(pat)])


# print(c1,c2)
for i in range(1, len(pat)):
    ans = max(ans, abs(c1[i] - c2[i + 1]) - 1)

print(ans)
