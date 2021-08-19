# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
from sys import stdin, stdout
import collections

#T = int(input())

#W,H = [int(x) for x in stdin.readline().split()]
#arr = [int(x) for x in stdin.readline().split()]

#s = input()
#N = len(s)

N, M, K = [int(x) for x in stdin.readline().split()]
arr = [int(x) for x in stdin.readline().split()]


res = 0
for j in range(M):
    s = 0
    mini = 0
    for i in range(j, N):
        if i % M == j:
            mini = min(mini, s)
            s -= K

        s += arr[i]

        res = max(res, s - mini)

print(res)
