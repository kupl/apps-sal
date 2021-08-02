'''input
111
'''
import math

string = input().strip()

xor = 0
for ele in string:
    xor ^= int(ele)

print("Exclusive" if xor == 0 else "Inclusive")
