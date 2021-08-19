import sys
n = int(input())
z = list(map(int, input().split()))
now = [0, 0]
for i in range(n):
    for j in range(n - i - 1):
        if z[j] > z[j + 1]:
            print(j + 1, j + 2)
            (z[j], z[j + 1]) = (z[j + 1], z[j])
