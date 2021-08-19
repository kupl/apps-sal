for _ in range(int(input())):
    (n, k) = map(int, input().split())
    for i in range(k - 1):
        n = str(n)
        if '0' in n:
            break
        n = int(n) + int(min(n)) * int(max(n))
    print(n)
