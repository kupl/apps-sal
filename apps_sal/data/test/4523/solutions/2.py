for _ in range(int(input())):
    n = int(input())
    s = sorted(map(int, input().split()))
    ans = 'YES'
    for i in range(1, n):
        if s[i] - s[i - 1] > 1:
            ans = 'NO'
            break
    print(ans)
