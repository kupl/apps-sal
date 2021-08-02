def busted_balls(balls, idx):
    # print(idx)
    busted = 2
    i = idx - 1
    j = idx + 2
    while(i >= 0 and j < len(balls) and balls[i] == balls[j]):
        while(i - 1 >= 0 and balls[i] == balls[i - 1]):
            i -= 1
        while j + 1 < len(balls) and balls[j] == balls[j + 1]:
            j += 1
        # print('i'+str(i))
        # print('j'+str(j))
        if j - i + 1 - busted >= 3:
            busted = (j - i + 1)
        else:
            break
        # print(busted)
        i -= 1
        j += 1
        # print('i'+str(i))
        # print('j'+str(j))
    return busted


n, k, x = list(map(int, input().split()))
balls = list(map(int, input().split()))
best = 0
for i in range(1, n):
    if balls[i] == balls[i - 1] and balls[i] == x:
        # copy_balls=balls[:]
        # copy_balls.insert(i)
        res = busted_balls(balls, i - 1)
        if(res > best):
            best = res
print(best)
