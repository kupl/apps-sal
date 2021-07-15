# -*- coding: utf-8 -*-
from decimal import Decimal  
import math

a, b = input().split()

a = int(a)
b = Decimal(b)

x = a * b

print((math.floor(int(a) * Decimal(b))))


