t = int(input())

for _ in range(t):
    a, b = map(int, input().split(' '))

    if a == b:
        print(0); continue
    
    if b > a:
        if a & 1 == b & 1:
            print(2); continue
        else:
            print(1); continue
    else:
        if a & 1 == b & 1:
            print(1); continue
        else:
            print(2); continue
