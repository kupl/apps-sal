n,k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

c = [i for i in a if i!=0]

if (c != sorted(c)):
    print("Yes")
else:
    if k == 1:
        for i in range(len(a)):
            if a[i] == 0:
                a[i] = b[0]
        if a == sorted(a):
            print("No")
        else:
            print("Yes")
    else:
        print("Yes")
        
    

