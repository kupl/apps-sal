from sys import stdin
input = stdin.readline

input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_only = b_only = 0
for i, j in zip(a, b):
    if i == j:
        continue
    if i == 1:
        a_only += 1
    elif j == 1:
        b_only += 1

if a_only == 0:
    print(-1)
else:
    print(b_only // a_only + 1)
