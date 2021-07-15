for _ in range(int(input())):
    n = list(map(int, input()))
    ans = []
    for i in range(len(n)):
        x = str(n[i]) + '0' * (len(n) - i - 1)
        x = int(x)
        if x != 0:
            ans.append(x)
    print(len(ans))
    print(*ans)
