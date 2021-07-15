T = int(input())
for t in range(T):
    h,n = list(map(int,input().strip().split(' ')))
    steps = list(map(int,input().strip().split(' ')))
    steps.append(0)
    cur = n
    danger = 0
    ret = 0
    index = 1
    cur = steps[index] + 1
    while cur > 2:
        if steps[index+1] == cur - 2:
            index += 2
        else:
            index += 1
            ret += 1
        cur = steps[index] + 1
    print(ret)

