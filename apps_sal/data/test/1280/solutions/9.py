import sys
import math as mt
t = 1
mod = 9007199254740881
for ___ in range(t):
    s1 = input()
    s2 = input()
    k = int(input())
    d = {}

    for i in range(len(s1)):
        suma = 0
        pre = 0
        D = 256
        for j in range(i, len(s1)):
            pre = (pre * D + ord(s1[j])) % mod
            posi = ord(s1[j]) - ord('a')
            if s2[posi] == '0':
                suma += 1
            if suma <= k:
                d[pre] = 1
            else:
                break
    print(len(d))
