# from collections import Counter
# from itertools import combinations
n = int(input())
doors = [int(i) for i in input().split()]
left = 0
right = 0
for i, door in enumerate(doors):
    if door == 0:
        right = i + 1
    else:
        left = i + 1
print(min(left, right))
