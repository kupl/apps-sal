for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = 0

    for i in range(n):
        if s[i] is '>':
            ans = i
            break

    for i in range(n - 1, -1, -1):
        if s[i] is '<':
            ans = min(n - 1 - i, ans)
            break

    print(ans)
