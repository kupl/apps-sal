import bisect as bs
N = input()
A = sorted([int(x) for x in input().split()])
ans = 0
def f(X, x): return bs.bisect_right(X, x) - bs.bisect_left(X, x)


for a in set(A):
    cnt = f(A, a)
    if cnt < a:
        ans += cnt
    else:
        ans += cnt - a
print(ans)
