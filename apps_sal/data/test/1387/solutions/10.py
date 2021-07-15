__author__ = 'Rakshak.R.Hegde'
"""
Created on Dec 30 2014 PM 08:30

@author: Rakshak.R.Hegde
"""


def mint(): return map(int, input().split())


n, t = mint()
a = list(mint())
curr = 1
while curr < t:
    curr = curr + a[curr - 1]
print('YES' if curr == t else 'NO')
