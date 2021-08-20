(n, k, m) = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = sum(arr)
i = 0
ans = -1
if n == 1:
    print(arr[0] + min(k, m))
else:
    elements = n
    while i < n - 1 and m > 0:
        avg1 = s + min(elements * k, m)
        avg1 = avg1 / elements
        avg2 = s - arr[i] + min((elements - 1) * k, m - 1)
        avg2 = avg2 / (elements - 1)
        if avg1 >= avg2:
            ans = max(avg1, ans)
        else:
            ans = max(avg2, ans)
        s -= arr[i]
        elements -= 1
        m -= 1
        i += 1
    print(ans)
