"""
Created on Oct 12, 2014

@author: Ismael
"""
from collections import Counter
from math import factorial, log, sqrt


def nbCombinations(r, n):
    return factorial(n) // factorial(r) // factorial(n - r)


s1 = input()
s2 = input()
counterS1 = Counter(s1)
counterS2 = Counter(s2)
if counterS1 == counterS2:
    print('1.000000000000')
elif '?' not in counterS2:
    print('0.000000000000')
else:
    nbPlusToMuch = counterS2['+'] - counterS1['+']
    nbMinusToMuch = counterS2['-'] - counterS1['-']
    if nbPlusToMuch > 0 or nbMinusToMuch > 0:
        print('0.000000000000')
    else:
        if nbPlusToMuch < 0:
            k = abs(nbPlusToMuch)
        else:
            k = abs(nbMinusToMuch)
        n = counterS2['?']
        print(nbCombinations(k, n) * 0.5 ** n)
