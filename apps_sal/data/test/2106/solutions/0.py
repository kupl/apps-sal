(n, k) = map(int, input().split())
(l, a) = (list(map(int, input().split())), list(map(int, input().split())))
(v, t, s) = (0, 0, sum(l))
for i in range(n):
    l[i] -= a[i]
(L, A) = ([l[0]], [a[0]])
for i in range(1, n):
    if a[i] <= A[-1]:
        L[-1] += l[i]
    else:
        A.append(a[i])
        L.append(l[i])
for i in range(len(A)):
    d = L[i] - v
    if d > 0:
        u = (d - 1) // A[i] + 1
        v += u * A[i]
        t += u * k
    v -= L[i]
print(t + s)
