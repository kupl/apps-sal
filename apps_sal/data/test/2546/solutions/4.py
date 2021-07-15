import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, s = list(map(int, input().split()))
    human = []
    x = n//2 + 1
    for _ in range(n):
        human.append(list(map(int, input().split())))

    human.sort(reverse = True)
    remain = s
    for i in range(n):
        remain -= human[i][0]

    right = 10**9+1
    left = 0
    while right - left > 1:
        mid = left + (right-left)//2
        count = 0
        money = remain
        for i in range(n):
            if human[i][1] < mid:
                continue
            elif human[i][0] >= mid:
                count += 1
                continue
            else:
                if money >= mid - human[i][0]:
                    money -= mid - human[i][0]
                    count += 1
                else:
                    break
        if count >= x:
            left = mid
        else:
            right = mid
    print(left)

