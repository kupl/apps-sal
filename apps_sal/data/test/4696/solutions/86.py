import sys
sys.setrecursionlimit(10**6)

a, b = list(map(int, input().split()))

if a * b % 2 == 0:
    print("Even")
else:
    print("Odd")
