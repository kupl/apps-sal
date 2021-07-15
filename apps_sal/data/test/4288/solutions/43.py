a,b,c = map(int,input().split())

if a == b == c:
    print("No")

elif a != b and b != c and a != c:
    print("No")

else:
    print("Yes")
