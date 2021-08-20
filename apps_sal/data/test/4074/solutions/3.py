for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    ar = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ar.append(i)
            ar.append(n // i)
        i += 1
    ar.sort()
    i = len(ar) - 1
    ans = n
    while i >= 0:
        if ar[i] <= k:
            ans = n // ar[i]
            break
        i -= 1
    print(ans)
