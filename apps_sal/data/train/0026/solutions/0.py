for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    if n < m:
        n, m = m, n # n > m

    if m == 1:
        print("YES")
        continue

    if m == 2 and n == 2:
        print("YES")
        continue

    print("NO")

