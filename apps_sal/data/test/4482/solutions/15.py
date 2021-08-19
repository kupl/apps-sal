import statistics
import math
n = int(input())
a = list(map(int, input().split()))
(ans1, ans2) = (0, 0)
a_avr1 = math.ceil(statistics.mean(a))
a_avr2 = math.floor(statistics.mean(a))
for i in range(n):
    ans1 += (a[i] - a_avr1) ** 2
    ans2 += (a[i] - a_avr2) ** 2
print(min(ans1, ans2))
