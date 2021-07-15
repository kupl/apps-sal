import os, sys, re, math

(N, M) = [int(n) for n in input().split()]

A = []
for i in range(N):
    A.append([i for i in range(10)])

answer = ''
for i in range(M):
    (s, c) = [int(n) for n in input().split()]
    if c in A[s - 1]:
        A[s - 1] = [c]
    else:
        answer = '-1'

if N > 1 and 0 in A[0]:
    A[0].remove(0)
    if not A[0]:
        answer = '-1'

if not answer:
    for i in range(N):
        answer += '%d' % min(A[i])

print(answer)

