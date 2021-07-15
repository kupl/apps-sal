for i in range(int(input())):
    if i :
        input()
    ans = []
    for i in range(8):
        s = input()
        for j in range(8):
            if s[j] == 'K':
                ans.append((i, j))
    print(['NO' , 'YES'][abs(ans[0][0] - ans[1][0]) % 4 == 0 and abs(ans[0][1] - ans[1][1]) % 4 == 0])

