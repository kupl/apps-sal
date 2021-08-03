for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    if n * m <= n + m:
        print("YES")
    else:
        print("NO")
