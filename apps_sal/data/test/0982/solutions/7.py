for t in range(int(input())):
    a, b = list(map(int, input().split()))
    print(["NO","YES"][a*2-1>=b])


