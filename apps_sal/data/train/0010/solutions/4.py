for _ in range(int(input())):
    n = int(input())
    p = tuple(map(int, input().split()))
    ans = [p[i] for i in range(n) if i in (0, n - 1) or p[i] != sorted(p[i - 1:i + 2])[1]]
    print(len(ans))
    print(*ans)

