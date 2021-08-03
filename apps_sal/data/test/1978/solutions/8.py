import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline
# print = stdout.write
def listin(): return list(map(int, input().split()))
def mapin(): return map(int, input().split())


n = int(input())
d = defaultdict(set)
for _ in range(n):
    z = input()
    for i in range(n):
        if z[i] == '1':
            d[_ + 1].add(i + 1)
m = int(input())
z = listin()
ans = [z[0]]
for i in range(1, m - 1):
    if z[i] in d[ans[-1]] and z[i + 1] in d[z[i]] and z[i + 1] not in d[ans[-1]] and ans[-1] != z[i + 1]:
        pass
    else:
        ans.append(z[i])
ans.append(z[-1])
print(len(ans))
print(*ans)
