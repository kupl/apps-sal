from bisect import bisect_right, insort_right
N = int(input())
A = [int(input()) for _ in range(N)][::-1]
res = [A[0]]
for a in A[1:]:
    idx = bisect_right(res, a)
    if idx == len(res):
        res.append(a)
    else:
        if res[idx] == a:
            insort_right(res, a)
        else:
            res[idx] = a
print((len(res)))
