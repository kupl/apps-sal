for _ in range(int(input())):
    (N, B) = map(int, input().split())
    ans = N - (N - 1) // B
    print(ans)
