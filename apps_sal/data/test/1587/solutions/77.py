import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
C = list(input().strip())

counter = Counter(C)
if len(counter) == 1:
    print(0)
else:
    red_n = counter["R"]
    ans = 0
    for i in range(N):
        if red_n <= i:
            break
        if C[i] == "W":
            ans += 1
    print(ans)
