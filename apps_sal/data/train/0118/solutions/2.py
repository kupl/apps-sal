for _ in range(int(input())):
    a,x = [int(a) for a in input().split(' ')]
    arr = [int(a) for a in input().split(' ')]
    arr = sorted(arr,reverse=True)
    cur_skill = x
    teams = 0
    cur_len = 0
    for i in arr:
        if i >= x:
            teams+=1
            continue
        else:
            cur_skill = i
            cur_len+=1
            if cur_len*cur_skill >= x:
                teams+=1
                cur_len = 0
                cur_skill = x

    print(teams)
