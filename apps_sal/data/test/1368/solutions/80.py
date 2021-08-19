import math
from collections import Counter
(N, A, B) = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse=True)
cnt_v = Counter(v)
ave = []
for i in range(A, B + 1):
    ave.append(sum(v[0:i]) / i)
max_ave = max(ave)
ans = 0
for j in range(B - A + 1):
    temp = 1
    if ave[j] == max_ave:
        l = v[:A + j]
        cnt_l = Counter(l)
        for (key, values) in cnt_l.items():
            temp *= math.factorial(cnt_v[key]) // math.factorial(values) // math.factorial(cnt_v[key] - values)
        ans += temp
print(max_ave)
print(ans)
