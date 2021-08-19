__author__ = 'Andrey'
n = int(input())
(m, s1) = (lambda x: (max(x), sum(x)))(list(map(int, input().split())))
s = s1 - m
print(m - s + 1)
