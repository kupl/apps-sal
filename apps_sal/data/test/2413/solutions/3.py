for _ in range(int(input())):
    n = int(input())
    s = input()
    if s == '0' * n:
        print(n)
    else:
        print(max(n - s.index('1'), s.rindex('1') + 1) * 2)
