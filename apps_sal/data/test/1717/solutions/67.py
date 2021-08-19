import math
N = int(input())
arr = [0] * (N + 1)
for i in range(2, N + 1):
    num = i
    for j in range(2, N + 1):
        count = 0
        while num % j == 0:
            num /= j
            count += 1
        arr[j] = max(arr[j], count)
ans = 1
for (j, v) in enumerate(arr):
    if v != 0:
        ans *= pow(j, v)
ans += 1
print(ans)
