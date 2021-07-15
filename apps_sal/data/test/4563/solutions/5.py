N = int(input())
Ratio = [tuple(map(int, input().split())) for _ in range(N)]
from math import ceil
Vote = (1, 1)
for t,a in Ratio:
    p = max((t+Vote[0]-1)//t, (a+Vote[1]-1)//a)
    Vote = (p*t, p*a)
print(sum(Vote))
