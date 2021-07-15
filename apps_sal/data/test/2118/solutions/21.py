import sys
def cal(l,r):
    nonlocal k
    if r-l < 2 or k == 0:
        return
    k -= 2
    m = (l+r)//2
    a[m], a[m-1] = a[m-1], a[m]
    cal(l,m)
    cal(m, r)
n, k = list(map(int,sys.stdin.readline().split()))
if k % 2 == 0:
    sys.stdout.write("-1")
else:
    k -= 1
    a = [i+1 for i in range(n)]
    cal(0, n)
    if k != 0:
        sys.stdout.write("-1")
    else:
        sys.stdout.write(' '.join([str(i) for i in a]))



