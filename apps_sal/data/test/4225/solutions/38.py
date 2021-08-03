import sys
A, B, C, K = [int(i) for i in input().split()]


if A >= K:
    print(K)
    return

r1 = K - A
cnt = A

if B >= r1:
    print(cnt)
    return

r2 = r1 - B
print((cnt - r2))
