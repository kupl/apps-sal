t = int(input())
for request in range(t):
    n = int(input())
    result, initial = list(map(int, input().split())), []
    box, flag = [], True
    initial.append(result[0])
    for d in range(1, result[0]):
        box.append(d)
    for i in range(1, n):
        if result[i - 1] < result[i]:
            initial.append(result[i])
            for d in range(result[i - 1] + 1, result[i]):
                box.append(d)
        else:
            try:
                initial.append(box.pop())
            except:
                flag = False
                break
    if flag:
        print(*initial)
    else:
        print(-1)
