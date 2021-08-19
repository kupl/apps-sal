import collections
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
A = collections.Counter(a)
B = collections.Counter(b)
inf = 1e+19
(cc, cd) = (0, 0)
R = 0
for i in range(n + 1):
    if A[i] + B[i] > n:
        R = inf
    else:
        cc += A[i]
        R = max(R, cc - cd)
        cd += B[i]
if R == inf:
    print('No')
else:
    print('Yes')
    ans = ' '.join(map(str, b[-R:] + b[:-R]))
    print(ans)
