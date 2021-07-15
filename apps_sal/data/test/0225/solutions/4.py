a,b,c,d = map(int, input().split())

tot = a+b+c+d

if tot % 2 == 1:
    print("NO")
    return

tot //= 2

if tot == a+b or tot == a+c or tot == a+d or tot == a or tot == b or tot == c or tot == d:
    print("YES")
else:
    print("NO")
