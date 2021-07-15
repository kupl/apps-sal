for _ in range(int(input())):
    a, b, n = list(map(int, input().split()))
    # n = int(input())
    # arr = list(map(int, input().split()))
    if a < b:
        a, b = b, a
    cnt = 0
    while a <= n:
        cnt += 1
        a, b = a + b, a
    print(cnt)


