l = input().split()
l = list(map(int, l))
l.sort()
if l[0] == l[1] == 5 and l[2] == 7:
    print("YES")
else:
    print("NO")
