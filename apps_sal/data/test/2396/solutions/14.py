from fractions import Fraction
n = int(input())
arr = []
cc = {}
for i in range(n):
    line = input()
    ab, c = line.split('/')
    ab = ab[1:-1]
    a, b = ab.split('+')
    a, b, c = [int(x) for x in (a, b, c)]
    p = (a + b) / c
    arr.append(p)
    if p not in cc:
        cc[p] = 1
    else:
        cc[p] += 1
for i in range(n):
    if i > 0:
        print(' ', end="")
    print(cc[arr[i]], end="")
