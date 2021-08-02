
def main():
    a, b = list(map(int, input().split()))
    if(a == 0 and b == 0):
        return 0
    x = 0
    y = 0
    step = 1
    rep = 0
    direction = 0
    ans = 0
    while(x != a or y != b):
        if(direction == 0):
            for i in range(step):
                x += 1
                if(x == a and y == b):
                    return ans
            direction = 1
            ans += 1
        elif(direction == 1):
            for i in range(step):
                y += 1
                if(x == a and y == b):
                    return ans
            direction = 2
            step += 1
            ans += 1
        elif(direction == 2):
            for i in range(step):
                x -= 1
                if(x == a and y == b):
                    return ans
            direction = 3
            ans += 1
        else:
            for i in range(step):
                y -= 1
                if(x == a and y == b):
                    return ans
            direction = 0
            step += 1
            ans += 1


print(main())
