import sys

n = int(input())

res = 0
for V in range(1, min(n, 8) + 1):
    for X in range(min(n - V, 4) + 1):
        res += n + 1 - V - X

for X in range(min(n, 8) + 1):
    res += n + 1 - X

print(res)
