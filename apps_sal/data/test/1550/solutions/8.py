__author__ = 'Rakshak.R.Hegde'
"""
Created on Dec 17 2014 PM 10:13

@author: Rakshak.R.Hegde
"""
n = int(input())
digits = list(map(int, input()))
enum = [[0] * n for i in range(10)]
enum[0] = digits
for i in range(1, 10):
    for j in range(n):
        enum[i][j] = (enum[i - 1][j] + 1) % 10
comp = []
for i in range(10):
    if enum[i][0] == 0:
        comp.append(enum[i])
    for j in range(1, n):
        if enum[i][j] == 0 and enum[i][j - 1] != 0:
            comp.append(enum[i][j:] + enum[i][:j])
print(''.join(map(str, min(comp))))
