import math
import bisect

n, m = map(int, input().split())
P = [int(c) for c in input().split()]
b_len = math.ceil(math.sqrt(n))
b = []
for i in range(1000):
    b.append(sorted(P[i * b_len:(i + 1) * b_len]))
    if n <= (i + 1) * b_len:
        break
b_cnt = len(b)
# print(b)

for i in range(m):
    l, r, x = map(int, input().split())
    l_b = (l - 1) // b_len
    r_b = (r - 1) // b_len

    if r_b - l_b <= 1:
        sorted_a = sorted(P[l - 1:r])
        print("Yes" if P[x - 1] == sorted_a[x - 1 - (l - 1)] else "No")
    else:
        _a = sorted(P[l - 1:(l_b + 1) * b_len] + P[r_b * b_len:r])
        # print(_a)
        idx = bisect.bisect_left(_a, P[x - 1])
        # print(idx)
        for j in range(l_b + 1, r_b):
            # print(b[j])
            idx += bisect.bisect_left(b[j], P[x - 1])
            # print(idx)
        print("Yes" if idx + l == x else "No")
