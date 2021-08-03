# Bhargey Mehta (Sophomore)
#DA-IICT, Gandhinagar
import sys
import math
import queue
#sys.stdin = open("input.txt", "r")
MOD = 10**9 + 7

n = int(input())
d = {}
for i in range(n):
    s = input()
    if s[0] in d:
        d[s[0]] += 1
    else:
        d[s[0]] = 1

ans = 0
for k in d:
    x1 = (d[k] + 1) // 2
    x2 = d[k] - x1
    ans += (x1 * (x1 - 1)) // 2 + (x2 * (x2 - 1)) // 2
print(ans)
