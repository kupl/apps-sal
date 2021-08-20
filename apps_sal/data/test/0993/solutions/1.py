from itertools import accumulate
(n, m) = map(int, input().split())
a = [0] + list(accumulate(map(int, input().split())))
di = {}
for i in a:
    i %= m
    if i not in di:
        di[i] = 0
    di[i] += 1
ans = 0
for i in di.values():
    ans += i * (i - 1) // 2
print(ans)
