x = int(input())
n = int(x**0.5)

if x==2 or x==3:
    print(x)
else:
    while True:
        for i in range(2,n+1,1):
            if x%i==0:
                break
        else:
            print(x)
            break
        x += 1
