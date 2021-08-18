import sys
import numpy as np
import math


sList = list(str(input()))
for i in range(3):
    if sList[i] == "1":
        sList[i] = "9"
    else:
        sList[i] = "1"

print("".join(sList))
