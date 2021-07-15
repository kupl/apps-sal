__author__ = 'User'
n, a, b = map(int, input().split())
a -= 1
a = (a + b) % n
a += 1
print(a)
