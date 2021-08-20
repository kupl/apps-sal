import bisect
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        k = bisect.bisect_left(arr, arr[i] + arr[j])
        if k > j:
            ans += k - j - 1
        else:
            pass
print(ans)
