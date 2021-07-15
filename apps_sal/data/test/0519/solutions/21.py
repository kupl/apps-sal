#In the name of Allah

from sys import stdin, stdout
input = stdin.readline

l = int(input())
p = int(input())
q = int(input())

stdout.write(str(p * q * l / (q) / (q + p)))

