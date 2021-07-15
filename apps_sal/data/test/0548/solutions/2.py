array_len = int(input())
idx___value = [int(x) for x in input().split()]
if sum(idx___value) % 2 != 0:
    print('First')
    return
    
lose_flag = True
for value in idx___value:
    if value % 2 != 0:
        lose_flag = False
        break
if lose_flag:
    print('Second')
    return
else:
    print('First')
    return
