N = int(input())
A = [int(a) for a in input().split()]
E = []
O = []
for a in A:
    if a % 2:
        O.append(a)
    else:
        E.append(a)
E = sorted(E)
O = sorted(O)
e = len(E)
o = len(O)
if e == o:
    print(0)
elif e < o:
    print(sum(O[:o - e - 1]))
else:
    print(sum(E[:e - o - 1]))
