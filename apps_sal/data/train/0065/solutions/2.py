for _ in range(int(input())):
    n = int(input())
    *difficulty, = list(map(int, input().split()))
    groups = [0]
    for i, v in enumerate(difficulty):
        if v == 0 and (i == 0 or difficulty[i - 1] == 1):
            groups.append(0)
        if v == 1:
            groups[-1] += 1
    ans = (groups[0] + 2) // 3 + sum(v // 3 for v in groups[1:])
    print(ans)
