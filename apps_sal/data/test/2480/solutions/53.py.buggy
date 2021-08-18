import sys

n, k = map(int, input().split())
a = [int(x) for x in input().split()]

values = dict()
valuelist = [0] * (n + 1)
values[0] = 1
s = 0
ans = 0
if k == 1:
    print(0)
    return

for i in range(n):
    s += a[i] - 1
    s %= k
    if s in values:
        ans += values[s]
        values[s] += 1
    else:
        values[s] = 1

    valuelist[i + 1] = s
    if i >= k - 2:
        values[valuelist[i - k + 2]] -= 1

print(ans)
