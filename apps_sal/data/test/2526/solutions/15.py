"""
Created on 2020/09/10

@author: harurun
"""


def main():
    import heapq
    import sys
    pin = sys.stdin.readline
    pout = sys.stdout.write
    perr = sys.stderr.write
    (X, Y, A, B, C) = list(map(int, pin().split()))
    p = list(map(int, pin().split()))
    q = list(map(int, pin().split()))
    r = list(map(int, pin().split()))
    p.sort(reverse=True)
    q.sort(reverse=True)
    r.sort(reverse=True)
    p = p[:X]
    q = q[:Y]
    Q = []
    for i in p:
        Q.append([i, 0])
    for j in q:
        Q.append([j, 1])
    heapq.heapify(Q)
    cntp = 0
    cntq = 0
    ans = 0
    for k in r:
        t = heapq.heappop(Q)
        if t[1] == 0 and t[0] < k and (cntp <= X):
            ans += k
            cntp += 1
        elif t[1] == 1 and t[0] < k and (cntq <= Y):
            ans += k
            cntq += 1
        else:
            ans += t[0]
            break
    while True:
        try:
            s = heapq.heappop(Q)
            ans += s[0]
        except:
            break
    print(ans)
    return


main()
