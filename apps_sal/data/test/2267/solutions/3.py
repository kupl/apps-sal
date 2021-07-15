from functools import cmp_to_key
import locale
def cmp(s, t):
    if s+t < t+s: return -1
    if s+t > t+s: return  1
    return 0

n = int(input())
S = [input() for i in range(n)]
S.sort(key = cmp_to_key(cmp))
print(''.join(S))

