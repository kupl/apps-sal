t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    if (a+b)%3 == 0 and 2*a-b >= 0 and 2*b-a >= 0:
        print("YES")
    else:
        print("NO")
