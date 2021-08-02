# import
#import math
#import numpy as np
N = int(input())
# = input()
# = map(int, input().split())
a = list(map(int, input().split()))
# = [input(), input()]
# = [list(map(int, input().split())) for _ in range(N)]
# = {i:[] for i in range(N)}

alen = N
two = 0
four = 0

for aa in a:
    if aa % 4 == 0:
        four += 1
    elif aa % 2 == 0:
        two += 1

other = alen - two - four

res = False

if other > four + 1:
    pass
elif other == four + 1:
    if two == 0:
        res = True
else:
    res = True

if res:
    print("Yes")
else:
    print("No")
