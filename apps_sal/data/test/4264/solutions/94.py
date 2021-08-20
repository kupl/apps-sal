import math
N = int(input())
m = int(math.log10(N)) + 1
a = N // pow(10, m)
ans = 0
for i in range(1, m, 2):
    ans += 9 * pow(10, i - 1)
if m % 2 == 1:
    ans += N - pow(10, m - 1) + 1
print(ans)
