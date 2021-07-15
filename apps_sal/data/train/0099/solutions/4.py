for test_i in range(int(input())):
    n = int(input())
    s = input()
    l1 = 0
    while l1 < n:
        if s[-l1 - 1] == '1':
            l1 += 1
        else:
            break
    l0 = 0
    while l0 < n:
        if s[l0] == '0':
            l0 += 1
        else:
            break
    if l0 + l1 < len(s):
        print('0' * (l0 + 1) + '1' * l1)
    else:
        print('0' * l0 + '1' * l1)
