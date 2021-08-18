m, n = map(int, input().split())

for i in range(m):
    if(i % 2 == 0):
        for i in range(n):
            print("
    else:
        for j in range(n):
            if(i % 4 == 1 and j == n - 1):
                print("
            elif(i % 4 == 3 and j == 0):
                print("
            else:
                print(".", end="")
    print("")
