for t in range(int(input())):
    x = input()
    ans = []
    for i in range(1,10):
        for j in range(1,5):
            ans.append(str(i)*j)
    cnt = 0
    for i in ans:
        if i==x:
            cnt+=len(i)
            break
        else:
            cnt+=len(i)
    print(cnt)
