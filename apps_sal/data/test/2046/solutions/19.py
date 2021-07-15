import sys
n = int(input())
a = list(map(int, input().split()))
b = list(reversed(sorted(a)))
has = set()
l = 0
for i in range(n):
    if a[i] == b[l]:
        has.add(a[i])
        while l < n and b[l] in has :
            print(b[l], end = ' ')
            l += 1
        print()
    else:
        has.add(a[i])
        print()
