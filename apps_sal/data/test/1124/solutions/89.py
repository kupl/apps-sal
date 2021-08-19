import sys
input = sys.stdin.readline

n = int(input())
a = set(map(int, input().split()))
a = list(a)
a.sort()
# print(a)

while len(a) > 1:
    d = set([a[0]])
    for ii in range(1, len(a)):
        if a[ii] % a[0] > 0:
            d.add(a[ii] % a[0])
    a = list(d)
    a.sort()

print(a[0])
