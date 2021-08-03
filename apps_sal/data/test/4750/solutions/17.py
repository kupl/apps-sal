for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if(a != c):
        print(a, c)
    elif(a != d):
        print(a, d)
    elif(b != c):
        print(b, c)
    elif(c != d):
        print(c, d)
