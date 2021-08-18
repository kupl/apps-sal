import sys
N = int(input())
d = list(map(int, input().split()))

K_cnt = 0
dsort = sorted(d)

d_left = dsort[int(N / 2) - 1]
d_right = dsort[int(N / 2)]

if d_left == d_right:
    print(0)
else:
    print(d_right - d_left)
