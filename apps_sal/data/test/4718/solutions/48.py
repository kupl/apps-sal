import sys
sys.setrecursionlimit(10**6)

s = list(str(input()))
s[:4] = list("2018")

print(("".join(s)))
