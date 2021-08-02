t = int(input(''))


def ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))


for _ in range(t):
    n = int(input(''))
    b = ternary(n)
    l = len(b)
    # print(b)
    ind = -1
    ans = ''
    for i in range(l):
        if(b[i] == '2'):
            ans = '0' * (l - i)
            ind = i
            break
    if(ind == 0):
        ans = '1' + ans
    elif(ind == -1):
        ans = b
    else:
        ind1 = -1
        for i in range(ind - 1, -1, -1):
            if(b[i] == '1'):
                ans = '0' + ans
            else:
                ans = '1' + ans
                ind1 = i
                break
        if(ind1 == -1):
            ans = '1' + ans
        else:
            ans = b[0:ind1] + ans

    print(int(ans, 3))
