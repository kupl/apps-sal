import sys
import math
n = int(input())
z = list(map(int, input().split()))
if n == 1:
    if z[0] == 0:
        print('UP')
        return
    if z[0] == 15:
        print('DOWN')
        return
    print(-1)
    return
if z[-1] == 0:
    print('UP')
    return
if z[-1] == 15:
    print('DOWN')
    return
z.append(z[-1] + z[-1] - z[-2])
if z[-1] > z[-2]:
    print('UP')
else:
    print('DOWN')
