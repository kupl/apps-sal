t = int(input())
for i in range(t):
    a = int(input())
    if a == 180:
        print(-1)
        break
    for j in range(3, 181):
        if a * j % 180 == 0:
            if j - (a * j // 180) == 1:
                j *= 2
            print(j)
            break
