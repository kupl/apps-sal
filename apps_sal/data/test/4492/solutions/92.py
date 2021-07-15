#coding: utf-8

N, X = (int(x) for x in input().split())
A = [int(x) for x in input().split()]

diffs = []
for i in range(N-1):
    diffs.append(A[i]+A[i+1] - X)

ret = 0
for i in range(N-1):
    tmp = min(diffs[i], A[i+1])
    ret += tmp
    diffs[i]   -= tmp
    if i+1 < len(diffs):
        diffs[i+1] -= min(tmp, diffs[i+1]) 
    ret += diffs[i]

print((max(0, ret)))


