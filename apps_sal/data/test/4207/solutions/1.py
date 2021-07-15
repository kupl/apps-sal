import collections
import math

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

arb = 0

counts = collections.defaultdict(int)

for x, y in zip(a, b):
    if x==0:
        if y==0:
            arb+=1
    else:
        if y==0:
            counts[(0, 0)] += 1
        else:
            if x<0 and y<0:
                x=-x
                y=-y
            elif x<0 and y>=0:
                x=-x
                y=-y
            g = math.gcd(x, -y)
            counts[(-y//g, x//g)] += 1

if counts:
    print(max(counts.values()) + arb)
else:
    print(arb)
