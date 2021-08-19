from itertools import accumulate
from bisect import bisect_left
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
(N, M) = map(int, input().split())
A = sorted(list(map(int, input().split())))
A_r = list(reversed(A))
B = [0] + list(accumulate(A_r))


def func(x):
    count = 0
    for Ai in A:
        idx = bisect_left(A, x - Ai)
        count += N - idx
    if count >= M:
        return True
    else:
        return False


MIN = 0
MAX = 2 * 10 ** 5 + 1
while MAX - MIN > 1:
    MID = (MIN + MAX) // 2
    if func(MID):
        MIN = MID
    else:
        MAX = MID
ans = 0
count = 0
for Ai in A_r:
    idx = bisect_left(A, MIN - Ai)
    ans += Ai * (N - idx) + B[N - idx]
    count += N - idx
print(ans - (count - M) * MIN)
