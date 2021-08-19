def __starting_point():
    N = int(input())
    li = list(map(int, input().split()))
    ans = [0] * (N + 1)
    for i in range(len(li)):
        ans[li[i]] += 1
    for i in range(1, N + 1):
        print(ans[i])


__starting_point()
