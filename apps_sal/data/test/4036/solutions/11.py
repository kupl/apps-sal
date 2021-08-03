import sys

n, k = map(int, input().split())
a = [0] * (k + 2)
if k * (k + 1) > n * 2:
    print("NO")
    return
for i in range(1, k + 1):
    a[i] = i
n -= k * (k + 1) // 2
rest = n // k
n -= rest * k
a[1] += rest
for i in range(2, k + 1):
    a[i] = a[i - 1] + 1
    rest = n // (k - i + 1)
    tmp = min(rest, a[i - 1] * 2 - a[i])
    a[i] += tmp
    n -= (k - i + 1) * tmp
if n > 0:
    print("NO")
    return
print("YES")
for i in range(1, k + 1):
    print(a[i], end=" ")
