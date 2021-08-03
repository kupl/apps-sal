n = int(input())
arr = [int(x) for x in input().split()]
pos = dict()
if(n == 1):
    print("B")
else:
    for i in range(n):
        pos[arr[i]] = i
    ans = ["Q"] * n

    ans[pos[1]] = "A"
    ans[pos[n]] = "B"
    for i in range(n - 1, 0, -1):
        flag = 0
        p = pos[i]
        j = 1
        while(p + j * i < n):
            if(ans[p + j * i] == "B"):
                flag = 1
                ans[pos[i]] = "A"
                break
            j += 1
        if(flag == 0):
            j = 1
            while(p - j * i >= 0):
                if(ans[p - j * i] == 'B'):
                    flag = 1
                    ans[pos[i]] = "A"
                    break
                j += 1
        if(flag == 0):
            ans[pos[i]] = "B"
    print("".join(ans))
