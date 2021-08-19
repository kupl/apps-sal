def main():
    import sys
    input = sys.stdin.readline
    (n, k) = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    arr.append(10 ** 12)
    median = arr[n >> 1]
    i = n // 2
    while i <= n - 1 and arr[i + 1] == median:
        i += 1
    cnt = i + 1 - n // 2
    while i <= n:
        i += 1
        while i <= n - 1 and arr[i + 1] == arr[i]:
            i += 1
        diff = arr[i] - median
        if diff * cnt > k:
            ans = median + k // cnt
            break
        else:
            median += diff
            k -= cnt * diff
            cnt = i + 1 - n // 2
    print(ans)
    return 0


main()
