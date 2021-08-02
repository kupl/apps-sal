import sys


def find_d(A):
    n = max(A) + 1
    A = [None] + A
    ind = [[] for _ in range(n)]
    for i in range(len(A)):
        if not A[i]:
            continue
        if len(ind[A[i]]) == 2:
            ind[A[i]][1] = i
        else:
            ind[A[i]].append(i)
    min_ind = len(A)
    d = 0
    for l in ind:
        if len(l) == 1:
            if l[0] < min_ind:
                min_ind = l[0]
            else:
                if d < l[0] - min_ind:
                    d = l[0] - min_ind
                    r = (d, min_ind)
        elif len(l) == 2:
            if d < l[1] - min_ind:
                d = l[1] - min_ind
                r = (d, min_ind)
            if l[0] < min_ind:
                min_ind = l[0]
        else:
            continue
    return d


n = int(sys.stdin.readline())
R = [int(i) for i in sys.stdin.readline().strip().split()]
R = [i - 100 for i in R]
S = []
s = 0
for i in range(n):
    s = s + R[i]
    S.append(s)
k = 0
d = 0
for i in range(len(S)):
    if S[i] > 0:
        k = i + 1
if any([x <= 0 for x in S]):
    s = 1 - min(S)
    S = [i + s for i in S]
    d = find_d(S)
print(max(d, k))
