#from functools import cmp_to_key
#from collections import deque
import math

mod = int(10**9+7)
N = int(1e5)+10

def main():
    d = {}
    for i in range(10):
        d[str(i)] = i
    i = 10
    for j in range(26):
        c = str(chr(ord('A')+j))
        d[c] = i
        i += 1
    for j in range(26):
        c = str(chr(ord('a') + j))
        d[c] = i
        i += 1
    d['-'] = i
    d['_'] = i+1
    s = input()

    ans = 1
    temp = [0 for i in range(64)]
    for i in range(64):
        for j in range(64):
            temp[i&j] += 1
    l = [d[c] for c in s]
    for j in l:
        ans = (temp[j]*ans+mod)%mod
    print(ans)


def __starting_point():
    main()
__starting_point()
