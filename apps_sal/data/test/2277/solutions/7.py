import sys

n = int(input())
a = [int(i) for i in input().split(" ")]
m = int(input())


inversion = 0

for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            inversion += 1

if inversion % 2:
    even = False
else:
    even = True

lines = sys.stdin.readlines()

for k in range(m):
    q = tuple(int(i) - 1 for i in lines[k].split(" "))

    if (((q[1] - q[0]) + 1) // 2) % 2:
        even = not even
    if even:
        print("even")
    else:
        print("odd")
