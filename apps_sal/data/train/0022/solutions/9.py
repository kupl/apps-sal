for _ in range(int(input())):
    a, k = list(map(int, input().split()))
    for _ in range(k - 1):
        mn = min(str(a))
        mx = max(str(a))
        if mn == "0":
            break
        a += int(mn) * int(mx)
    print(a)
