import sys
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())

def rep_xor(x):
    if x%4 == 0:
        return 0^x
    elif x%4 == 1:
        return 1
    elif x%4 == 2:
        return 1^x
    else:
        return 0

if a > 0:
    fa = rep_xor(a-1)
    fb = rep_xor(b)
    ans = fa^fb
else:
    fb = rep_xor(b)
    ans = fb

print(ans)
