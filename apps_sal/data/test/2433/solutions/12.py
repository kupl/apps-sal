import sys 
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()

for t in range(int(input())):
  b, p, f = list(map(int, input().split()))
  h, c = list(map(int, input().split()))

  if h >= c:
    beef = min((b//2), p)
    b -= beef * 2
    chicken = min((b//2), f)
    print(beef*h + chicken*c)
  else:
    chicken = min((b//2), f)
    b -= chicken * 2
    beef = min((b//2), p)
    print(beef*h + chicken*c)

