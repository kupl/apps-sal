for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    i = 0
    teams = 0
    teamMem = 0
    while (i < len(arr)):
        if ((teamMem + 1) * arr[i] >= k):
            teams += 1
            teamMem = 0
        else:
            teamMem += 1
        i += 1
        # print(teams,teamMem)
    print(teams)
