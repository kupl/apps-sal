from itertools import accumulate
n = int(input())
s = [0 if i == 'E' else 1 for i in str(input())]
s_cumsum = list(accumulate(s))
s_cumsum_rev = list(accumulate(reversed(s)))
ans = 10 ** 10
for i in range(1, n - 1):
    a_1 = s_cumsum[i - 1]
    a_0 = i - a_1
    b_1 = s_cumsum_rev[-2 - i]
    b_0 = n - 1 - i - b_1
    ans = min(ans, a_1 + b_0)
ans = min(ans, s_cumsum[-2])
ans = min(ans, n - 1 - s_cumsum_rev[-2])
print(ans)
