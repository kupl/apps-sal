for _ in range(int(input())):
    n = int(input())
    s = input()
    if n == 1:
        print(s)
        continue
    zero = -1
    one = -1
    for i in range(n):
        if s[i] == '0':
            zero = i
        if s[i] == '1' and one < 0:
            one = i
    if zero < one or one == -1 or zero == -1:
        print(s)
    else:
        print((one + 1) * '0' + (n - zero - 1) * '1')
