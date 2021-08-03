n = int(input())
arr = list(map(int, input().split()))

n25 = 0
n50 = 0
poss = True
for i in range(n):
    if(arr[i] == 25):
        n25 += 1
    elif(arr[i] == 50):
        n50 += 1
        n25 -= 1
    else:
        if(n50 > 0):
            n25 -= 1
            n50 -= 1
        else:
            n25 -= 3
    if(n25 < 0 or n50 < 0):
        poss = False
print('NO' if not poss else 'YES')
