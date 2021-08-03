import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

a, b = list(map(int, input().split()))

bt = 0
if b % 2:
    bt = ((b + 1) // 2) % 2
else:
    bt = (b // 2) % 2
    bt ^= b

at = 0
if (a - 1) % 2:
    at = (a // 2) % 2
else:
    at = ((a - 1) // 2) % 2
    at ^= (a - 1)

print((bt ^ at))
