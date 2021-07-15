q=int(input())
for i in range(q):
    ints=[int(x) for x in input().split()]
    n=ints[0]
    k=ints[1]
    if k % 3 == 0:
        if (n % (k+1)) % 3 != 0 or (n % (k+1)) == k:
            print("Alice")
        else:
            print("Bob")
    else:
        if n % 3 == 0:
            print("Bob")
        else:
            print("Alice")
