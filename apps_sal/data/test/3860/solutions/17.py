import sys 
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()

b = int(input())
g = int(input())
n = int(input())

ans = 0 
for i in range(n + 1):
  if i <= b and n - i <= g:
    ans += 1

print(ans)

