import math

def solve(n, k, s):
    i, j = s.index('G'), s.index('T')
    if (i - j) % k != 0:
        return False
    for k in range(i, j, (k if i < j else -k)):
        if k >= n or k < 0 or s[k] == '#':
            return False
    return True

n, k = [int(x) for x in input().split()]
s = input()
print('YES' if solve(n, k, s) else 'NO')
    

