# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 20:30:05 2015

@author: kevin
"""

tableautaille = input().split(" ");

n = int(tableautaille[0])
m = int(tableautaille[1])
tabfinal = []
for i in range(n):
    tab = input().split(" ")
    c = int(tab[0])
    t = int(tab[1])
    tabfinal += [c * t]

tableau = input().split(" ");
res = 0
indice = 0
for i in range(m):
    search = int(tableau[i])
    while(search > res + tabfinal[indice]):
        res += tabfinal[indice]
        indice += 1
    print(indice + 1)
