import re
import math
import decimal
import bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)


# code goes here
n = iread()
seq = "".join([str(v) for v in viread()])
zs = seq.count("0")
os = seq.count("1")
for j, i in enumerate(seq):
    if i == "0":
        zs -= 1
    else:
        os -= 1
    if zs == 0 or os == 0:
        print(j + 1)
        return
