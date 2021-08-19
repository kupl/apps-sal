for _ in range(int(input())):
    (a, b) = list(map(int, input().split()))
    ans = 0
    for i in range(a - 1):
        s = input()
        if s[-1] != 'D':
            ans += 1
    s = input()
    for i in range(b - 1):
        if s[i] != 'R':
            ans += 1
    print(ans)
