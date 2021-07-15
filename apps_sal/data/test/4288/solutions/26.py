
l = list(map(int,input().split()))

if l[0] == l[1] == l[2]:
    print("No")
elif l[0] == l[1] or l[0] == l[2] or l[1] == l[2]:
    print("Yes")
else:
    print("No")
