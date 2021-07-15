s = list(map(int,input().split()))
a = s[0]
b = s[1]
x = s[2]
y = s[3]

if a == b:
    print(x)
elif a < b:
    print(min(x+(b-a)*y,((b-a)*2+1)*x))
else:
    print(min(((a-b)*2-1)*x,x+(a-b-1)*y))
