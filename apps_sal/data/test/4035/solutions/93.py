import math
(A, B) = map(int, input().split())
p1 = 0.08
p2 = 0.1
a_l = math.ceil(A / p1)
a_r = math.floor((A + 1) / p1)
b_l = math.ceil(B / p2)
b_r = math.floor((B + 1) / p2)
if b_r <= a_l or a_r <= b_l:
    print(-1)
else:
    print(max(a_l, b_l))
