__author__ = 'Rakshak.R.Hegde'
"""
Created on Jan 12 2015 PM 02:32

@author: Rakshak.R.Hegde
"""

a, b, c, d = map(int, input().split())
pA = max((3 * a) // 10, a - (a * c) // 250)
pB = max((3 * b) // 10, b - (b * d) // 250)
if pA == pB:
    print('Tie')
else:
    print('Misha' if pA > pB else 'Vasya')
