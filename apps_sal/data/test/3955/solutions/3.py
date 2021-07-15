__author__ = 'kitkat'
import sys

#sys.stdin = open("in.txt")
try:
    while True:
        n, k, x = list(map(int, input().split(" ")))
        val = [0] + list(map(int, input().split(" ")))
        res = 0
        L = [0 for i in range(200003)]
        R = [0 for i in range(200003)]
        for i in range(1, n+1, 1):
            L[i] = L[i-1] | val[i]
            R[n-i+1] = R[n-i+2] | val[n-i+1]
        for i in range(1, n+1, 1):
            for j in range(k):
                val[i] *= x
        for i in range(1, n+1, 1):
            res = max(res, L[i-1] | R[i+1] | val[i])
        print(res)
except EOFError:
    pass

