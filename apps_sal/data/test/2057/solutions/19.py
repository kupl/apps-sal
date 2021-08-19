import fractions
import math
n = int(input())
t = list(map(int, input().split(' ')))
a = set(t)
print(n + 1 - len(a))
