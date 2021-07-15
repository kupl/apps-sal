input_ar = list(map(int,input().rstrip().split(" ")))
leaders = list(map(int,input().rstrip().split(" ")))
not_there_set = {i+1 for i in range(input_ar[0])}
a_n_done = [False for i in range(input_ar[0])]
a_n = [0 for i in range(input_ar[0])]
possible = True
for i in range(len(leaders) - 1):
    diff = leaders[i + 1] - leaders[i]
    if diff <= 0:
        diff += input_ar[0]
    if a_n[leaders[i] - 1] is 0:
        if diff in a_n:
            possible = False
            break
        not_there_set.remove(diff)
        a_n[leaders[i] - 1] = diff
    elif a_n[leaders[i] - 1] is not diff:
        possible = False
        break

if not possible:
    # print(a_n)
    print(-1)
else:
    # print('a_n is : {}'.format(a_n))
    for i in range(len(a_n)):
        if a_n[i] is 0:
            if len(not_there_set) <= 0:
                possible = False
                break
            a_n[i] = not_there_set.pop()
    if not possible:
        print(-1)
    else:
        for a in a_n:
            print('{} '.format(a), end='')
        print()
