for i in range(int(input())):
    (n, l, r) = map(int, input().split())
    print('No') if n // l < n / r else print('Yes')
