for _ in range(int(input())):
    a, b = map(int, input().split())
    if(b < a):
        a, b = b, a
    i = 0
    while(a != b):
        if(8 * a <= b):
            a *= 8
            i += 1
        elif(4 * a <= b):
            a *= 4
            i += 1
        elif(2 * a <= b):
            a *= 2
            i += 1
        else:
            i = -1
            break
    print(i)
