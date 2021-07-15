for __ in range(int(input())):
    n, k = list(map(int, input().split()))
    ar = list(map(int, input().split()))
    ar.sort(reverse=True)
    ans = 0
    for i in range(min(n, k + 1)):
        ans += ar[i]
    print(ans)
