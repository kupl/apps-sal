from math import sqrt

n = int(input())
A = list(map(int, input().split()))
print(max(a for a in A if a < 0 or int(sqrt(a))**2 != a))
