__author__ = 'Rakshak.R.Hegde'
"""
Created on Dec 24 2014 PM 10:22

@author: Rakshak.R.Hegde
"""

n, m = map(int, input().split())
trans = dict()
for i in range(m):
    x, y = input().split()
    trans[x] = y
lect = input().split()
ans = ''
for w in lect:
    ans += min(w, trans[w], key=lambda x: len(x)) + ' '
print(ans)
