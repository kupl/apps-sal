import math
import sys
import string
input = sys.stdin.readline
#letters = list(string.ascii_lowercase)

t = int(input())
for i in range(t):
    n = list(map(int, input().split()))
    ans = abs(n[0] - n[2]) * abs(n[3] - n[1])
    print(ans + 1)
