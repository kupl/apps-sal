for i in range(int(input())):
    a = int(input())
    m = bin(a)
    k = 1
    for i in m[2:]:
        if i == '1':
            k *= 2
    print(k)
