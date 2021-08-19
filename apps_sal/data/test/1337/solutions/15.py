import sys
import math
n = int(input())
uch = list(map(int, sys.stdin.readline().split()))
dic = dict()
for x in uch:
    if x in list(dic.keys()):
        dic[x] += 1
    else:
        dic[x] = 1
m = int(input())
langf = list(map(int, sys.stdin.readline().split()))
subf = list(map(int, sys.stdin.readline().split()))
maxl = 0
maxs = 0
ans = 1
for i in range(m):
    if langf[i] not in list(dic.keys()):
        dic[langf[i]] = 0
    if subf[i] not in list(dic.keys()):
        dic[subf[i]] = 0
    if maxl < dic[langf[i]]:
        maxl = dic[langf[i]]
        maxs = dic[subf[i]]
        ans = i + 1
    elif maxl == dic[langf[i]] and maxs < dic[subf[i]]:
        maxs = dic[subf[i]]
        ans = i + 1
print(ans)
