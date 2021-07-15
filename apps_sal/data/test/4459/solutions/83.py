N = input()
A = sorted([int(x) for x in input().split()])
import bisect as bs
ans = 0
f = lambda X, x: bs.bisect_right(X,x) - bs.bisect_left(X,x)
for a in set(A):
    cnt = f(A,a)
    if cnt < a:
        ans += cnt
    else:
        ans += cnt-a
print(ans)
