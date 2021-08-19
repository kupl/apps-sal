n = int(input())
arr = list(map(int, input().split()))
ans = 0
b = 2 ** (n + 1) - 3
while n != 0:
    n -= 1
    # print(n)
    p = 2 ** (n + 1) - 3
    while b != p:
        ans += abs(arr[b] - arr[b - 1])
        arr[b // 2 - 1] += max(arr[b], arr[b - 1])
        # print(arr)
        b -= 2
print(ans)
