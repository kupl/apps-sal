from collections import defaultdict
N = int(input())
arr = defaultdict(int)
for i in range(2, N + 1):
    temp = i
    f = True
    for j in range(2, int(-(-i**0.5 // 1)) + 1):
        if temp % j == 0:
            cnt = 0
            while temp % j == 0:
                cnt += 1
                temp //= j
            f = False
            arr[j] += cnt
    if temp != 1:
        f = False
        arr[temp] += 1
    if f:
        arr[i] += 1
ans = 1
for i in arr.values():
    ans *= i + 1
    ans %= 10**9 + 7
print(ans)
