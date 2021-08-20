import sys
N = input()
L = list(map(int, input().split()))
L.sort(reverse=True)
a = L[1::2]
s = 0
for x in a:
    s += x
print(s)
