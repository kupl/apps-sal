import sys

n, m = list(map(int, input().split()))

for i in range(n):
    for c in input().split():
        if c not in ['W', 'G', 'B']:
            print("#Color")
            return

print("#Black&White")
