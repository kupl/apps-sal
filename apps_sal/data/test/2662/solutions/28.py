from bisect import bisect_right
(N, *A) = list(map(int, open(0).read().split()))
A = [-a for a in A]
q = []
for a in A:
    idx = bisect_right(q, a)
    if idx == len(q):
        q.append(a)
    else:
        q[idx] = a
print(len(q))
