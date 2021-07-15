for i in range(int(input())):
    a, b = list(map(int,input().split()))
    if a > 2 and b >= 2 or b > 2 and a >= 2:
        print("NO")
    else:
        print("YES")

