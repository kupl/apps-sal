#!/usr/bin/env python3
import sys

def rint():
    return list(map(int, sys.stdin.readline().split()))
#lines = stdin.readlines()

n = int(input())
s = input()

o = s.count('(')
c = s.count(')')
ans = []
cnt = 0

ok = 0
for i in range(n):
    ans.append(s[i])

oc = o - c
if oc > 0:
    for i in range(n-1, -1, -1):
        if oc == 0:
            break
        if ans[i] =='?':
            ans[i] = ')'
            oc -= 1
    if oc !=0:
        print(':(')
        return
#print(ans)
qc = n - o - c - (o-c)
#print(qc)
if qc%2:
    print(':(')
    return

q = 0
for i in range(n):
    if q == qc:
        break
    if ans[i] == '?':
        if q < qc//2:
            ans[i] = '('
        else:
            ans[i] = ')'
        q += 1
#print(ans)
cnt = 0
for i in range(n):
    if ans[i] == '(':
        cnt += 1
    elif ans[i] == ')':
        cnt -= 1
    if cnt <= 0 and i != n-1:
        print(':(')
        return
#print(cnt)
if cnt != 0:
    print(':(')
    return
print(''.join(ans))





