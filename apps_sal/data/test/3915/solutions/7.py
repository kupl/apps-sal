"""
Created on 19 Aؤںu 2015

@author: enesoncu
"""
pr = [0] * 1300000


def prime():
    pr[1] = 1
    for i in range(2, 1300000):
        if pr[i] == 1:
            continue
        for j in range(2 * i, 1300000, i):
            pr[j] = 1


def palindrom(s):
    s = str(s)
    return s == s[::-1]


(p, q) = list(map(int, input().split()))
res = 'Palindromic tree is better than splay tree'
rub = 0
pi = 0
prime()
for i in range(1, 1200000):
    if pr[i] == 0:
        pi += 1
    if palindrom(i):
        rub += 1
    if pi * q <= rub * p:
        res = i
print(res)
