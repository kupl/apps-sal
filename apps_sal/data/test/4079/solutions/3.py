# Bhargey Mehta (Sophomore)
#DA-IICT, Gandhinagar
import sys
import math
import queue
sys.setrecursionlimit(1000000)
#sys.stdin = open("input.txt", "r")

for i in range(int(input())):
    x = []
    s = input()
    for c in s:
        x.append(ord(c))
    x.sort()
    ans = "Yes"
    for i in range(1, len(x)):
        if x[i] != x[i - 1] + 1:
            ans = "No"
            break
    print(ans)
