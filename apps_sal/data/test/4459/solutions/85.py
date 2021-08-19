import collections
n = int(input())
A = list(map(int, input().split()))
C = collections.Counter(A)
ans = 0
for (k, v) in C.items():
    if k == v:
        continue
    elif k < v:
        ans += v - k
    else:
        ans += v
print(ans)
