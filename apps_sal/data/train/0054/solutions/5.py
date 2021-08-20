t = int(input())
for nt in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    new = []
    for i in l:
        if i <= 2048:
            new.append(i)
    new.sort()
    if 2048 in new:
        print('YES')
    else:
        s = 0
        flag = 0
        for i in range(len(new) - 1, -1, -1):
            s += new[i]
            if s == 2048:
                print('YES')
                flag = 1
                break
        if flag == 0:
            print('NO')
