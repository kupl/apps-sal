''' بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ '''
def gi(): return list(map(int, input().split()))


for k in range(gi()[0]):
    n, = gi()
    l = gi()
    cl = l[l.index(1):] + l[:l.index(1)]
    ccl = l[l.index(n):] + l[:l.index(n)]
    p = [i for i in range(1, n + 1)]
    if cl == p or ccl == p[::-1]:
        print("YES")
    else:
        print("NO")
