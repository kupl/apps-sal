from bisect import bisect_right
(N, M, Q) = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(M)]
lr.sort(reverse=True)
lst = [[]]
j = N - 1
for i in range(M):
    if lr[i][0] - 1 < j:
        lst[-1].sort()
        while lr[i][0] - 1 < j:
            lst.append(lst[-1][:])
            j -= 1
    lst[-1].append(lr[i][-1] - 1)
lst[-1].sort()
lst.reverse()
for i in range(Q):
    (p, q) = map(int, input().split())
    m = bisect_right(lst[p - 1], q - 1)
    print(m)
