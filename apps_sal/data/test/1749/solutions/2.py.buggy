import sys

n, l, r = list(map(int, (sys.stdin.readline()).split(" ")))
a = list(map(int, (sys.stdin.readline()).split(" ")))
b = list(map(int, (sys.stdin.readline()).split(" ")))
l -= 1
for i in range(0, l):
    if a[i] != b[i]:
        print("LIE")
        return
for i in range(r, n):
    if a[i] != b[i]:
        print("LIE")
        return
print("TRUTH")
