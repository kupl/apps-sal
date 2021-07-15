nb_cups, nb_task = [int(x) for x in input().split()]
caffines = sorted([int(x) for x in input().split()], reverse=True)
if nb_task > sum(caffines):
    print(-1)
else:    
    for days in range(1, 101):
        task_done = 0
        for curr in range(nb_cups):
            task_done += max(0, caffines[curr] - curr // days)
        if task_done >= nb_task:
            print(days)
            break

