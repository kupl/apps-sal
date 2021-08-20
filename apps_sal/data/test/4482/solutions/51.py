from sys import stdin
input = stdin.readline
N = int(input())
A = list(map(int, input().split()))
if len(set(A)) != 1:
    cost = 2 ** 20
    for i in range(-100, 101):
        tc = 0
        for a in A:
            tc += (a - i) ** 2
        if cost > tc:
            cost = tc
else:
    cost = 0
print(cost)
