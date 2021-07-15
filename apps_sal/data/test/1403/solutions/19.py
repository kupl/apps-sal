#!/usr/bin/env python3
from sys import stdin, stdout

def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


n, K = rint()

a = list(rint())

a.sort()
#print(K)
#print(a)

cnt = 0
cnt_same = 1
for i in range(n-1):
    if a[i+1] == a[i]:
        cnt_same += 1
        continue
    if a[i+1] - a[i] <= K:
        cnt_same = 1
        continue
    else:
        cnt += cnt_same
        cnt_same = 1

#print(cnt, cnt_same)
print(cnt+ cnt_same)



