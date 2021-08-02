import sys

n, k = map(int, input().split())
a = list(map(int, input().split()))
setofa = set(a)
s = []
f = False
ai = 0
ans = []
for i in range(1, n + 1):
    if i in setofa:
        while ai < k and (len(s) == 0 or s[-1] != i):
            s.append(a[ai])
            ai += 1
        if len(s) == 0 or s[-1] != i:
            f = True
            break
        s.pop(-1)
        a += ans[::-1]
        ans = []
    else:
        if ai != k:
            s += a[ai:k]
            ai = k
        ans.append(i)

if f:
    print(-1)
else:
    print(' '.join(map(str, a + ans[::-1])))
