"""
Created on 19.03.2014

@author: mboeschen
"""
import sys
inp = sys.stdin
x = inp.readline()
n = int(x)
ls = []
for i in range(n):
    ls.append(inp.readline())
a = ls[0][0]
b = ls[0][1]
Answer = True
if a == b:
    Answer = False
for i in range(n):
    for j in range(n):
        if i == j or n - i - 1 == j:
            if ls[i][j] != a:
                Answer = False
        elif ls[i][j] != b:
            Answer = False
if Answer:
    print('YES')
else:
    print('NO')
