a,b = (int(x) for x in input().split())
tmp = a//b
if tmp%2 == 0:
    print("NO")
else:
    print("YES")
