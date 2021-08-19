for __ in range(int(input())):
    n = list(input())
    num = 0
    for elem in n:
        num += int(elem)
    if '0' in n and num % 3 == 0 and ('2' in n or '4' in n or '6' in n or ('8' in n) or (n.count('0') >= 2)):
        print('red')
    else:
        print('cyan')
