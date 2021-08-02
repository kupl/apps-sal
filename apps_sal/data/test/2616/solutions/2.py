tests = int(input())
for t in range(tests):
    n = int(input())
    ls = list(map(int, input().split()))
    count_one = 0
    for item in ls:
        if item == 1:
            count_one += 1
        else:
            break
    if count_one != n:
        if count_one % 2 == 1:
            print('Second')
        else:
            print('First')
    else:
        if count_one % 2 == 1:
            print('First')
        else:
            print('Second')
