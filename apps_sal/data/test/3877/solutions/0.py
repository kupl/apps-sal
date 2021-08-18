
import sys
input = sys.stdin.readline

n, l, r = list(map(int, input().split()))

a1 = 0

layers = 1
while layers * 2 <= n:
    layers *= 2

for i in range(l, r + 1):
    layer = layers
    while i % 2 == 0:
        layer //= 2
        i //= 2
    if (n // layer) % 2 == 1:
        a1 += 1

print(a1)
