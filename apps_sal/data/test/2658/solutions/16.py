def __starting_point():
    """
    1 2 3 4 5 6 5
    2 3 4 2 3 4 2
    """
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    start = 1

    loop_start = 0
    loop_end = 0

    steps = []
    steps_map = {}

    steps.append(start)

    cur = start
    for i in range(n):
        cur = a[cur-1]
        if cur in steps_map:
            loop_start = steps_map[cur] # 1
            loop_end = i+1  # 4
            break
        else:
            steps.append(cur)
            steps_map[cur] = i+1
    
    # print(loop_start, loop_end)
    # print(steps)
    if(k <= loop_start):
        print((steps[k]))
    else:
        temp = (k - loop_start) % (loop_end - loop_start)
        print((steps[temp + loop_start]))



__starting_point()
