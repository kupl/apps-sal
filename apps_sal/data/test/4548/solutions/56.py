import numpy as np

n, m, x = map(int, input().split())
a = list(map(int, input().split()))

a = np.array(a)

ans = min(len(a[a < x]), len(a[a > x]))
print(ans)
