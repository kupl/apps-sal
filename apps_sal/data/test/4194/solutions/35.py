n, m = map(int, input().split())
aa = list(map(int, input().split()))

homework = sum(aa)


if n < homework:
    print(-1)
else:
    print(n - homework)
