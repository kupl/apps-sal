from bisect import bisect
arr = []
n = 1
while 1:
    v = n * (n + 1) // 2 * 3 - n
    if v > 10 ** 9:
        break
    arr.append(v)
    n += 1
T = int(input())
for _ in range(T):
    N = int(input())
    ans = 0
    while N >= 2:
        i = bisect(arr, N)
        v = arr[i - 1]
        N -= v
        ans += 1
    print(ans)
