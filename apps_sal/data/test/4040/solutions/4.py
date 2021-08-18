n, m, d = list(map(int, input().split()))
plank = list(map(int, input().split()))
summ = sum(plank)
j = 0
ans = [0] * n
curr = -1
i = 0
flag = 0
while(i < n):
    if(summ == n - i):
        if(j == m):
            print("NO")
            flag = 1
            break
        for _ in range(plank[j]):
            ans[i] = j + 1
            i = i + 1
        summ = summ - plank[j]
        j = j + 1
        curr = i - 1
    elif(i - curr == d):
        if(j == m):
            flag = 1
            print("NO")
            break
        for _ in range(plank[j]):
            ans[i] = j + 1
            i = i + 1
        summ = summ - plank[j]
        j = j + 1
        curr = i - 1
    else:
        i = i + 1
if(flag == 0):
    print("YES")
    print(*ans)
