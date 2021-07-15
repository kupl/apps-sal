for _ in  range(int(input())):
    word = input()
    temp = []
    for i in range(len(word)):
        if word[i]=='1':
            temp.append(i)
    ans = 0
    for i in range(1,len(temp)):
        ans+=(temp[i]-temp[i-1]-1)
    print(ans)
