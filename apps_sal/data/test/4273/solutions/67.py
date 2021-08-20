from itertools import combinations
n = int(input())
Mnum = 0
Anum = 0
Rnum = 0
Cnum = 0
Hnum = 0
for i in range(n):
    a = input()
    if a[0] == 'M':
        Mnum += 1
    elif a[0] == 'A':
        Anum += 1
    elif a[0] == 'R':
        Rnum += 1
    elif a[0] == 'C':
        Cnum += 1
    elif a[0] == 'H':
        Hnum += 1
alist = []
alist.append(Mnum)
alist.append(Anum)
alist.append(Rnum)
alist.append(Cnum)
alist.append(Hnum)
print(sum([a * b * c for (a, b, c) in combinations(alist, 3)]))
