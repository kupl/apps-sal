from math import *
from sys import *
from decimal import *


def gcd(a, b):
    if b:
        return gcd(b, a % b)
    return a


mat = []
for i in range(4):
    mat.append(input())
for st in mat:
    if ("xx." in st) or (".xx" in st) or ("x.x" in st):
        print("YES")
        return
for i in range(4):
    st = ""
    for j in range(4):
        st += mat[j][i]
    if ("xx." in st) or (".xx" in st) or ("x.x" in st):
        print("YES")
        return
for su in range(2, 5):
    st = ""
    for j in range(max(0, su - 3), min(su + 1, 4)):
        st += mat[j][su - j]
    if ("xx." in st) or (".xx" in st) or ("x.x" in st):
        print("YES")
        return
for ee in range(-1, 2):
    st = ""
    for j in range(max(0, -ee), min(4, 4 - ee)):
        st += mat[j][j + ee]
    if ("xx." in st) or (".xx" in st) or ("x.x" in st):
        print("YES")
        return
print("NO")
