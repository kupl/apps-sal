from decimal import *
import math

a, b = list(map(Decimal, input().split()))
print((math.floor(a * b)))
