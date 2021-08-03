# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:38:18 2015

@author: kebl4230
"""
aa = [int(num) for num in input().split()]
books = [int(num) for num in input().split()]
result = 0
for genre in range(1, aa[1] + 1):
    n = books.count(genre)
    aa[0] -= n
    result += n * aa[0]
print(result)
