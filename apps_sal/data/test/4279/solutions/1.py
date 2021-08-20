"""
Created on 2019. 9. 21.

@author: kkhh88
"""
s = ''
le = [0]
for i in range(1, 22000):
    s = s + str(i)
    le.append(le[-1] + len(s))


def sol(k):
    d = 0
    for i in range(1, 22000):
        if le[i] > k:
            d = i - 1
            break
    k = k - le[d]
    if k == 0:
        return str(d)[-1]
    else:
        return s[k - 1]


n = int(input())
for i in range(n):
    print(sol(int(input())))
