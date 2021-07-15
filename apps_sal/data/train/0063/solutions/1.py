for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    # n = int(input())
    arr = list(map(int, input().split()))
    wrr = list(map(int, input().split()))
    wrr.sort()
    arr.sort()
    ans = 0
    for i in range(k):
        ans += arr[-1]
        wrr[i] -= 1
        if wrr[i] == 0:
            ans += arr[-1]
        arr.pop()
    i = 0
    j = 0
    wrr.sort(reverse=True)
    while i < len(arr) and j < len(wrr):
        if wrr[j] == 0:
            j += 1
        else:
            ans += arr[i]
            i += wrr[j]
            wrr[j] = 0
    print(ans)

