def solve(n, m, w, l):
    low = min(l)
    high = max(l) + m
    while low < high:
        mid = (low + high + 1) // 2
        val = 0
        arr = [0 for i in range(w + n)]
        for i in range(n):
            val += arr[i]
            arr[i + w] -= max(0, mid - l[i] - val)
            val -= arr[i + w]
        if -sum(arr) > m:
            high = mid - 1
        else:
            low = mid
    print(low)


(n, m, w) = map(int, input().split())
l = [*map(int, input().split())]
solve(n, m, w, l)
