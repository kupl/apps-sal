
t = int(input())

for loop in range(t):

    a,b,c,n = list(map(int,input().split()))

    n -= max(a,b,c) - a
    n -= max(a,b,c) - b
    n -= max(a,b,c) - c

    if n >= 0 and n % 3 == 0:
        print ("YES")
    else:
        print ("NO")

