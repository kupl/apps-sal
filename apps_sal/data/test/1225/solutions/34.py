import sys

H = int(input())
i = 0
n = 0
while True:
    if 2**i > H:
        break
    n += 2**i
    i += 1

print(n)

