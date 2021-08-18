import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline
def listin(): return list(map(int, input().split()))
def mapin(): return map(int, input().split())


n = int(input())
a = listin()
z = a[0]
for i in range(1, n):
    z = math.gcd(z, a[i])
d = defaultdict(int)
while(z % 2 == 0):
    z //= 2
    d[2] += 1
for i in range(3, int(z**0.5) + 1, 2):
    while(z % i == 0):
        z //= i
        d[i] += 1
if z > 1:
    d[z] += 1
ans = 1
for i in d.values():
    ans *= (i + 1)
print(ans)
