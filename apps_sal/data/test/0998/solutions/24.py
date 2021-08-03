import math
from sys import stdin
# stdin=open('input.txt')


def input():
    return stdin.readline().strip()


# from sys import stdout
# stdout=open('input.txt',mode='w+')

# def print1(x, end='\n'):
# 	stdout.write(str(x) +end)


# a, b = map(int, input().split())

# l = list(map(int, input().split()))


# CODE BEGINS HERE.................


n, x = list(map(int, input().split()))

seen = [False] * (2**(18))
seen[0] = True
seen[x] = True

a = []
pref_sum = 0
for i in range(2**n):
    if seen[i]:
        continue
    a.append(pref_sum ^ i)
    pref_sum = i
    seen[i] = True
    seen[x ^ i] = True
print(len(a))
print(*a)

# CODE ENDS HERE....................
# stdout.close()
