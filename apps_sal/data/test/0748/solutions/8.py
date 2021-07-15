n = int(input())
arr = list(map(int, input().split()))
mp = dict()
mp[1] = 0
mp[2] = 0
mp[3] = 0
mp[4] = 0
mp[6] = 0
for num in arr:
    if num == 1:
        mp[1] = mp[1] + 1
    elif num == 2:
        mp[2] = mp[2] + 1
    elif num == 3:
        mp[3] = mp[3] + 1
    elif num == 4:
        mp[4] = mp[4] + 1
    elif num == 6:
        mp[6] = mp[6] + 1

sum0 = 0
sum1 = 0
sum2 = 0

if mp[1] != n//3:
    print(-1)
else:
    while True:
        flag = True
        if mp[2] > 0 and mp[4] > 0:
            sum0 = sum0 + 1
            flag = False
            mp[2] = mp[2] - 1
            mp[4] = mp[4] - 1
        elif mp[2] > 0 and mp[6] > 0:
            sum1 = sum1 + 1
            flag = False
            mp[2] = mp[2] - 1
            mp[6] = mp[6] - 1
        elif mp[3] > 0 and mp[6] > 0:
            sum2 = sum2 + 1
            flag = False
            mp[3] = mp[3] - 1
            mp[6] = mp[6] - 1
        if flag == True:
            break
        
    if sum0 + sum1 + sum2 != n//3:
        print(-1)
    else:
        for i in range(sum0):
            print(1, " ", 2, " ", 4)
        for i in range(sum1):
            print(1, " ", 2, " ", 6)
        for i in range(sum2):
            print(1, " ", 3, " ", 6)
        

