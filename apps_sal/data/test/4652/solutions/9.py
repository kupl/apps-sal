for _ in range(int(input())):
    n = int(input())
    ans = [i + 1 for i in range(n)]
    l = list(map(int, input().split()))
    one = l.index(1)
    l = l[one:] + l[:one]
    rev = l[::-1]
    one = rev.index(1)
    rev = rev[one:] + rev[:one]
    if rev == ans or l == ans:
        print('YES')
    else:
        print('NO')
