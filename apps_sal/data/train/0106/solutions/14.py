T = int(input())
for i in range(T):
    n = int(input())
    inp = []
    temp = []
    for j in range(n):
        a, b = [int(u) for u in input().split()]
        inp.append([a, b])
        temp.append([a, b])
    inp.sort()
    check = 0
    begin = inp[0][0]
    end = inp[0][1]
    for j in range(n):
        if(inp[j][0] > end):
            check = 1
            break
        if(inp[j][1] > end):
            end = inp[j][1]
    ans = []
    if(check == 0):
        print(-1)
    else:
        for j in range(n):
            if(temp[j][0] >= begin and temp[j][1] <= end):
                ans.append("1")
            else:
                ans.append("2")
        print(" ".join(ans))
