for _ in range(int(input())):
    n = int(input())
    l = []
    for i in str(n):
        l.append(i)
    ans = []
    l = l[-1::-1]
    cnt = 0
    for i in l:
        if i != '0':
            ans.append(int(i) * pow(10, cnt))
            cnt += 1
        else:
            cnt += 1
    print(len(ans))
    print(*ans)
    # print(l)
