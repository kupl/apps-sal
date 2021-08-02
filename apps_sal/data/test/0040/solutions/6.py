from sys import stdin
input = stdin.readline

n = int(input())

change = 0
unordered = 0
c = float('inf')
for i in range(n):
    a, b = [int(x) for x in input().split()]
    if a != b:
        change = 1
        break
    elif c < a:
        unordered = 1
    c = a

if change:
    print('rated')
elif unordered:
    print('unrated')
else:
    print('maybe')
