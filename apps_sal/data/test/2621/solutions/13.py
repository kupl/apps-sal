t = int(input())

for _ in range(t):
    n, m, k = list(map(int, input().split()))
    h = list(map(int, input().split()))

    result = True
    for i in range(n - 1):
        if h[i + 1] - h[i] > k + m:
            result = False
            break
        elif h[i] + k > h[i + 1]:
            m += h[i] - h[i + 1] + min(k, h[i + 1])
        elif h[i + 1] > h[i] + k:
            m -= h[i + 1] - h[i] - k
            if m < 0:
                result = False
                break
        else:  # ==
            pass

    if result:
        print("YES")
    else:
        print("NO")
