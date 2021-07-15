while True:
    n = int(input())
    path = list(map(int, input().split()))

    eleminatedY = {1}
    y = 1

    for i in range(n - 1):

        diff = abs(path[i] - path[i + 1])

        if diff == 0:
            print("NO");return

        if diff == 1:
            eleminatedY.add(min(path[i], path[i + 1]))
            if min(path[i], path[i + 1]) % y == 0 and y != 1:
                print("NO");return
            continue

        if y == diff:
            continue

        for value in eleminatedY:
            if value % diff == 0:
                print("NO");return

        if y == 1:
            y = diff
            continue
        
        print("NO");return

    print("YES\n{} {}".format(1000000000, y))
            
    return

