__author__ = 'Andrey'
n = int(input())
k = n // 7
c = n % 7
print(2 * k + max(0, c - 5), 2 * k + min(c, 2))
