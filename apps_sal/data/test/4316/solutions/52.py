a = list(input())
if(len(a) > 4):
    stop()
a.sort()
if(a[0] == a[1] and a[2] == a[3] and a[0] != a[2]):
    print("Yes")
else:
    print("No")
