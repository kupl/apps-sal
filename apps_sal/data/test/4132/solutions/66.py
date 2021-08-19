import numpy as np
n = int(input())
a = list(map(int, input().split()))
ans = a[0]
for i in range(1, len(a)):
    ans = np.gcd(a[i], ans)
print(ans)
