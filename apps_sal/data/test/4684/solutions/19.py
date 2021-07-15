r, g, b = map(str, input().split())

sumstr = r + g + b
sumint = int(sumstr)

if sumint % 4 == 0:
    print("YES")
else:
    print("NO")
