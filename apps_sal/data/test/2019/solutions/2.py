for _ in range(int(input())):
    ar = list(input())
    x, y = ar.count('0'), ar.count('1')
    if min(x, y) % 2 == 1:
        print('DA')
    else:
        print('NET')
