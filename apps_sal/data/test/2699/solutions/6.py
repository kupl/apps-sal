# cook your dish here
t = int(input())
ar = list(map(int, input().split()))
for i in ar:
    z = 3
    a = 1
    for j in range(i):
        print(str(a),end=' ')
        a = a+z
        z = 2*z
    print('\r')
    z = 3
    a = 2
    for j in range(i):
        print(str(a),end=' ')
        a = a+z
        z = 2*z
    print('\r')
    z = 6
    a = 4
    for j in range(i):
        print(str(a),end=' ')
        a = a+z
        z = 2*z
    print('\r')
    z = 3
    a = 3
    for j in range(i):
        print(str(a),end=' ')
        a = a+z
        z = 2*z
    print('\r')
