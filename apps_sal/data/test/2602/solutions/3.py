for _ in range(int(input())):
    (a, b, n, m) = list(map(int, input().split()))
    if n + m > a + b or m > min(a, b):
        print('No')
    else:
        print('Yes')
