s,t = input().split()
a,b = map(int,input().split())
u = input()

if u == s:
    a = a - 1
    print(a,b)

elif u == t:
    b = b - 1
    print(a,b)
