from collections import Counter
N = int(input())
Alist = []
maxi = 0
n2 = 0
for _ in range(N):
    A = int(input())
    Alist.append(A)
    if A > maxi:
        n2 = maxi
        maxi = A
    elif A > n2:
        n2 = A
count = Counter(Alist)
for A in Alist:
    if A != maxi:
        print(maxi)
    elif A == maxi and count[A] > 1:
        print(maxi)
    else:
        print(n2)
