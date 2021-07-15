n = int(input())

if n == 1:
    print(n)
    print(1)
elif n <= 3:
    print(n - 1)
    out = "1"
    for i in range(3,n+1,2):
        out += " " + str(i)
    print(out)
elif n == 4:
    print(4)
    print("3 1 4 2")
else:
    print(n)
    out = "1"
    for i in range(3,n+1,2):
        out += " " + str(i)
    for i in range(2,n+1,2):
        out += " " + str(i)
    print(out)

