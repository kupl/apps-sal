n, k, q = [int(s) for s in input().split()]
friend_list = [int(s) for s in input().split()]
active_friends_id = dict()

active_friends = [-1 for i in range(k)]
min_value = 0
min_ind = -1
min_key = -1
count = 0
tmp_ind = 0
for i in range(q):
    req, id = [int(s) for s in input().split()]
    id -= 1
    if req == 1:
        if count != k or friend_list[id] > min_value:
            if count == k:
                active_friends_id[min_ind] = id
                active_friends[min_ind] = friend_list[id]
                min_value = min(active_friends)
                min_ind = active_friends.index(min_value)
            else:
                active_friends_id[tmp_ind] = id
                active_friends[tmp_ind] = friend_list[id]
                tmp_ind += 1
                count += 1
                if count == k:
                    min_value = min(active_friends)
                    min_ind = active_friends.index(min_value)
    else:
        if id in active_friends_id.values():
            print("YES")
        else:
            print("NO")
