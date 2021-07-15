a,b,c = list(map(int,(input().split())))

ans = 0

ans = a+b+c

if ans > 21:
    print("bust")
else:
    print("win")

