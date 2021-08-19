__author__ = 'PrimuS'
n = int(input())
i = 0
k = 0
m = 0
while n >= 0:
    i += 1
    m += i
    k += m
    n -= m
print(i - 1)
