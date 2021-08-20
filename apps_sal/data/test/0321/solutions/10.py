def prime(x):
    if x == 1:
        return False
    ret = True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            ret = False
    return ret


n = int(input())
for i in range(n):
    s = input().split()
    d = int(s[0]) - int(s[1])
    if d != 1:
        print('NO')
    elif prime(int(s[0]) + int(s[1])):
        print('YES')
    else:
        print('NO')
