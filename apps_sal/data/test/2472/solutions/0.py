def solve(N, ABs):
    ABs.sort(key=lambda x: x[1])
    time = 0
    ans = 'Yes'
    for (A, B) in ABs:
        time += A
        if time > B:
            ans = 'No'
            break
    print(ans)


def __starting_point():
    N = int(input())
    ABs = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, ABs)


__starting_point()
