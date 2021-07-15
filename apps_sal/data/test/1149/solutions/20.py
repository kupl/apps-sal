import math
import time

n = int(input())
a1 = list(map(int, input().split(' ')))
a2 = list(map(int, input().split(' ')))

a1.remove(a1[0])
a2.remove(a2[0])

for i in range(n):
    index = i+1
    found = a1.count(index)+a2.count(index)
    if found == 0:
        print("Oh, my keyboard!")
        return

print("I become the guy.")
