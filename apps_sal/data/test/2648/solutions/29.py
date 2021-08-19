from collections import Counter
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
L = len(Counter(A))
if L % 2 == 0:
    print(L - 1)
else:
    print(L)
