#!/usr/bin/env python3

n, k, d = list(map(int, input().split()))
if k ** d < n:
    print(-1)
else:
    for i in range(d):
        p = k ** i
        arr = [j // p % k + 1 for j in range(n)]
        print(' '.join(map(str, arr)))
