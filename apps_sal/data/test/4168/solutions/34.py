N = int(input())


def calc(x):
    ans = ''
    while True:
        if x % 2 == 0:
            ans = '0' + ans
        else:
            ans = '1' + ans
            x -= 1
        if x == 0:
            break
        x = x // -2
    return ans


a = calc(N)
print(a)
