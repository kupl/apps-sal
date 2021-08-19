import math
(n, x) = map(int, input().split())
a = list(map(int, input().split()))
a.append(x)
a = sorted(a)
diff_list = [0] * n
for i in range(1, n + 1):
    diff_list[i - 1] = a[i] - a[i - 1]
g = diff_list[0]
for i in range(1, n):
    g = math.gcd(g, diff_list[i])
print(g)
