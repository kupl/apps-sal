"""
Codeforces Contest 291 Div 2 Problem A

Author  : chaotic_iak
Language: Python 3.4.2
"""

################################################### SOLUTION

def main():
    s = read(0)
    t = ""
    for i in range(len(s)):
        t += str(min(int(s[i]), 9-int(s[i])))
    if t[0] == "0": t = "9" + t[1:]
    print(t)


#################################################### HELPERS



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
