import sys
n = int(input())
z = list(map(int, input().split()))
a = max(z) * n
print(a - sum(z))
