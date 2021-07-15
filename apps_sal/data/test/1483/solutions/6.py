from sys import stdin
from math import *

line = stdin.readline().rstrip().split()
n = int(line[0])

numbers = list(map(int, stdin.readline().rstrip().split()))



for i in range(n):
    point = i + 1
    holed = [False] * n
    while not holed[point-1]:
        holed[point-1] = True
        point = numbers[point-1]
    print(point, end=" ")


