(n, size, tasks) = map(int, input().split())
friends = list(map(int, input().split()))
online = list()
for i in range(tasks):
    (type, id) = map(int, input().split())
    id -= 1
    if type == 1:
        adds = friends[id]
        online = sorted(online + [adds], reverse=True)
        if len(online) > size:
            del online[-1]
    else:
        flag_oh_my_god_why = False
        search = friends[id]
        for bear in online:
            if bear == search:
                flag_oh_my_god_why = True
                break
        if flag_oh_my_god_why == False:
            print('NO')
        else:
            print('YES')
