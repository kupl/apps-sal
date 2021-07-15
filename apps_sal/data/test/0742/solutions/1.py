# Код программы написал на языке Python 3
import sys
import bisect

def main():
    n =  int(sys.stdin.readline())
    q = [int(i) for i in sys.stdin.readline().split()]
    w = []
    for i in range(1, 2 * n + 1):
        if i not in q:
            w.append(i)
    w.sort()
    res = [0 for i in range(2*n)]
    for i in range(n):
        res[i * 2] = q[i]
    for i in range(n - 1):
        e = bisect.bisect(w, q[i])
        if e != n - i:
            r = w[e]
            del w[e]
            res[i * 2 + 1] = r
        else:
            print(-1)
            return 0
    if w[-1] < q[-1]:
        print(-1)
        return 0
    else:
        res[-1] = w[-1]
        print(*res)
    
        
for test in range(int(sys.stdin.readline())):
    main()
