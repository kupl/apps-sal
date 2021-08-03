n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

left4seat = n
left2seat = n * 2
left1seat = 0
for i in range(0, k):
    left4seat -= a[i] // 4
    if (left4seat < 0):
        left2seat += 2 * left4seat
        left4seat = 0

index = 0
while (index < k):
    leftSol = a[index] % 4
    if (leftSol == 3):
        if (left4seat > 0):
            left4seat -= 1
        else:
            if (left1seat > 0):
                if (left2seat == 0 and left1seat >= 2):
                    left1seat -= 3
                else:
                    left2seat -= 1
                    left1seat -= 1
            else:
                left2seat -= 2
    elif (leftSol == 2):
        if (left4seat > 0):
            left4seat -= 1
            left1seat += 1
        else:
            if (left2seat == 0 and left1seat >= 2):
                left1seat -= 2
            else:
                left2seat -= 1
    elif (leftSol == 1):
        if (left1seat > 0):
            left1seat -= 1
        elif (left4seat > 0):
            left4seat -= 1
            left2seat += 1
        else:
            left2seat -= 1
    if (left4seat < 0 or left2seat < 0):
        break
    index += 1

if (index == k and left4seat >= 0 and left2seat >= 0):
    print("YES")
else:
    print("NO")
