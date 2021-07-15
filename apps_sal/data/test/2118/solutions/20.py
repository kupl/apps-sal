from sys import setrecursionlimit as c
c(10000)
 
def s(a, le, ri):
    nonlocal k
    if k <= 0 or le >= ri-1:
        return
    k -= 2
    mid = (le+ri)//2
    a[mid], a[mid-1] = a[mid-1], a[mid]
    s(a, le, mid)
    s(a, mid, ri)
 
n, k = list(map(int, input().split()))
 
if not(k%2):
    print("-1")
else:
    k -= 1
    l = list(range(1, n+1))
    s(l, 0, n)
    if not(k):
        print(*l)
    else:
        print("-1")

