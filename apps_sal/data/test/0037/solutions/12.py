import collections
import math

a, b, c = list(map(int, input().split()))
#n = int(input())
for i in range(c // a + 1):
    if (c - a * i) % b == 0:
        print('Yes')
        return
print('No')


