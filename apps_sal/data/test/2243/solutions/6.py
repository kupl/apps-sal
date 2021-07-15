

listed = list()

n, k, q= list(map(int,input().split()))


def del_minv():
    nonlocal listed
    minv = 0
    for _ in range(len(listed)):
        if friend_value[listed[_]] < friend_value[listed[minv]]:
            minv = _
    del listed[minv]


friend_value = list(map(int, input().split()))
friend_online = [False]*len(friend_value)

for _ in range(q):
    query = list(map(int,input().split()))
    query[1] -= 1

    if query[0] == 1:
        friend_online[query[1]] = True
        listed.append(query[1])
        if len(listed) > k: del_minv()
        #print(listed)
    else:
        print('YES') if query[1] in listed else print('NO')



