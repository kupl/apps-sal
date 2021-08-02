for _ in range(int(input())):
    n = int(input())
    L = list(map(int, input().split()))
    ans = 0
    for i in range(len(L)):
        if L[i] == 0:
            ans += 1
            L[i] = 1

    if sum(L) == 0:
        ans += 1

    print(ans)
