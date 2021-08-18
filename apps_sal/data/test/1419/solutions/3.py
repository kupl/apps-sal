def check(xs, k, t):
    l = 1
    tmp = 0
    for x in xs:
        if(x > t):
            return False
        tmp += x
        if(tmp > t):
            tmp = x
            l += 1
    if l > k:
        return False
    else:
        return True


k = int(input())
xs = list([len(list(x)) + 1 for x in input().replace('-', ' ').split()])
xs[-1] -= 1

up = sum(xs)
down = 1
ans = (up + down) // 2
while down + 1 < up:
    ans = (down + up) // 2
    if check(xs, k, ans):
        up = ans
    else:
        down = ans

print(up)
