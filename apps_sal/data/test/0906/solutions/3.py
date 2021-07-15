ins = [int(x) for x in input().split(" ")]
n = ins[0]
m = ins[1]
k = ins[2]
big = 1000000007

if n == 1:
    if k == 1:
        print("1")
    if k == -1:
        if m % 2 == 1:
            print("1")
        else:
            print("0")
elif m == 1:
    if k == 1:
        print("1")
    if k == -1:
        if n % 2 == 1:
            print("1")
        else:
            print("0")
else:
    if k == -1:
        if n%2 != m%2:
            print("0")
        else:
            print(pow(2,(n-1)*(m-1),big))
    else:
        print(pow(2,(n-1)*(m-1),big))

