'''
Created on Oct 6, 2014

@author: Ismael
'''
n = int(input())
A = list(map(int,input().split()))
q = int(input())
Q = list(map(int,input().split()))
ans = []
prec = 1
iStack = 0
for ai in A:
    iStack += 1
    for query in range(prec,prec+ai):
        ans.append(iStack)
    prec = ai
for query in Q:
    print(ans[query-1])
