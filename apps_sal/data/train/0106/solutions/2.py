t = int(input())
for i in range(t):
    n = int(input())
    sobs = []
    for j in range(n):
        a, b = list(map(int, input().split()))
        sobs.append([[a, -1], j])
        sobs.append([[b, 1], j])
    sobs.sort()
    counts = 0
    passed = []
    success = []
    alls = [0 for q in range(n)]
    succeed = False
    for sob in sobs:
        if succeed:
            if sob[0][1] == -1:
                pass
            else: 
                success.append(sob[1])
            continue
        if sob[0][1] == -1:
            counts += 1
        else:
            counts -= 1
            passed.append(sob[1])
            if counts == 0:
                succeed = True
    if succeed and success:
        for a in passed:
            alls[a] = 1
        for b in success:
            alls[b] = 2
        print(*alls)
    else:
        print(-1)

