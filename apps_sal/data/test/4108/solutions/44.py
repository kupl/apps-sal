import collections
a = list(input())
b = list(input())
A = collections.Counter(a)
B = collections.Counter(b)
Alist = list(A.values())
Blist = list(B.values())
Asort = sorted(Alist)
Bsort = sorted(Blist)
if Asort == Bsort:
    print("Yes")
else:
    print("No")
