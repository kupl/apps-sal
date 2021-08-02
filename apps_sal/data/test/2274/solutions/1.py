for _ in range(int(input())):
    n, m = map(int, input().split())
    ans = 0
    for i in range(n - 1):
        s = input()
        if s[-1] == 'R': ans += 1
    ans += input()[:-1].count('D')
    print(ans)
