def resolve():
    a = []
    bingo = [(0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6)]
    for _ in range(3):
        a += list(map(int, input().split()))
    for i in range(int(input())):
        r = int(input())
        if r in a:
            a[a.index(r)] = 0
    ans = 'No'
    for i in bingo:
        if a[i[0]] == 0 and a[i[1]] == 0 and a[i[2]] == 0:
            ans = 'Yes'
    print(ans)


resolve()
