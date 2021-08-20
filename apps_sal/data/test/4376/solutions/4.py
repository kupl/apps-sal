from bisect import bisect_left
from itertools import accumulate
(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s_a = [0] + list(accumulate(a))
ans = list()
for el in b:
    ind = bisect_left(s_a, el)
    num = el - s_a[ind - 1]
    ans.append(f'{ind} {num}')
print('\n'.join(ans))
