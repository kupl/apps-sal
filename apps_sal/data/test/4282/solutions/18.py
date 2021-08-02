import sys
input = sys.stdin.readline

n = int(input())
P = [list(map(int, input().split())) for i in range(n)]

x, y = P[0]

if y in P[x - 1]:
    print(1, x, end=" ")
    n = x
    nn = y
else:
    print(1, y, end=" ")
    n = y
    nn = x

while nn != 1:
    k, u = P[n - 1]
    print(nn, end=" ")
    if k == nn:
        n, nn = nn, u
    else:
        n, nn = nn, k
