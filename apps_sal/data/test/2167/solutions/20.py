"""input
6
-1 1 0 0 -1 -1
"""
n = int(input())
a = list(map(int, input().split()))
print(n if sum(a) % n == 0 else n - 1)
