a,b,c,d = map(int,input().split())


if a == b:
    print(c)
    return

if a < b:
    print(min(c+d*(b-a), c+2*c*(b-a)))
else:
    print(min(c+d*(a-b-1), c+2*c*(a-b-1)))
