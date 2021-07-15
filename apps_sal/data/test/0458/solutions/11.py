"""
Codeforces Contest 262 Div 2 Problem B

Author  : chaotic_iak
Language: Python 3.3.4
"""

def main():
    a,b,c = read()
    res = []
    for i in range(1, 82): # max is 999999999
        x = b * (i**a) + c
        if x <= 0 or x >= 10**9: continue
        if sum(map(int, list(str(x)))) == i: res.append(x)
    res.sort()
    print(len(res))
    print(" ".join(map(str, res)))

################################### NON-SOLUTION STUFF BELOW

def read(mode=2):
    # 0: String
    # 1: List of strings
    # 2: List of integers
    inputs = input().strip()
    if mode == 0: return inputs
    if mode == 1: return inputs.split()
    if mode == 2: return list(map(int, inputs.split()))

def write(s="\n"):
    if s is None: s = ""
    if isinstance(s, list): s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")

write(main())
