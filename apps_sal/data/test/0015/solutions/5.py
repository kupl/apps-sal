a,b,c = map(int, input().split())

if c == 0 :
    ans = (a == b)
else :
    k = (b - a)//c
    ans = (k >= 0 and a + c*k == b)

if ans :
    print("YES")
else :
    print("NO")
