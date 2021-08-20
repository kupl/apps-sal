q = int(input())
for i in range(q):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    flag = 0
    for i in range(len(l) - 1):
        if l[i + 1] - l[i] == 1:
            flag = 1
            break
    if flag:
        print(2)
    else:
        print(1)
