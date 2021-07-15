for _ in range(int(input())):
    a, b, c = list(map(int, input().split()))
    ans = 0
    ans += min(b, c//2)*3
    b-=min(b, c//2)
    ans+=min(a, b//2)*3
    print(ans)
