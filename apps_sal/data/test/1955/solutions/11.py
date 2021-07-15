"""
Brandt Smith, Peter Haddad, Lemuel Gorion

Codeforces.com

Problem 732D
"""
import sys

n, m = list(map(int, input().split(' ')))
di = list(map(int,input().split(' ')))
ai = list(map(int,input().split(' ')))

completed = [False] * m 

summ = sum(ai) + m
temp = m

for i in range(n):
    if di[i] == 0:
        continue
    else:
        if not completed[di[i] - 1]:
            if ai[di[i] - 1] <= i:
                temp -= 1
                completed[di[i] - 1] = True

        if temp == 0:
            if i + 1 >= summ:
                print(i + 1)
                return

print(-1)


