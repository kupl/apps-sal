k = list(map(int, input().strip().split()))
k = sorted(k)

if k[0] == 1:
    print("YES")
elif k[0] == 2 and k[1] == 2:
    print("YES")
elif k[0] == 2 and k[1] == 4 and k[2] == 4:
    print("YES")
elif k[0] == 3 and k[1] == 3 and k[2] == 3:
    print("YES")
else:
    print("NO")



