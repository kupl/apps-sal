__author__ = 'Alexander'


n, a, b = map(int, input().split())

t = input()

if t[a - 1] != t[b - 1]:
    print(1)
else:
    print(0)
