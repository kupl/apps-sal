for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if sum(a) % x != 0:
        print(n)
        continue
    printed = False
    for i in range(n):
        if a[i] % x != 0 or a[-i - 1] % x != 0:
            print(n - i - 1)
            printed = True
            break
    if not printed:
        print(-1)
