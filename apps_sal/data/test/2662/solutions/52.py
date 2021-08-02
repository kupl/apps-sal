from bisect import bisect_right
N = int(input())
A = [int(input()) for _ in range(N)]
ans = 1
min_vs = [A[-1]]
for i in range(N - 2, -1, -1):
    a = A[i]
    idx = bisect_right(min_vs, a)
    if idx == len(min_vs):
        ans += 1
        min_vs.append(a)
    else:
        min_vs[idx] = a
print(ans)
