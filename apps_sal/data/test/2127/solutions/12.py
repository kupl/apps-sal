import sys
input = sys.stdin.readline
n = int(input())
a = [list(map(str,input().split())) for _ in range(n)]
tate = 0
yoko = 0
for i in range(n):
    if a[i][0] == "+":
        b = [int(a[i][1]),int(a[i][2])]
        b.sort()
        if tate < b[0]:
            tate = b[0]
        if yoko < b[1]:
            yoko = b[1]
    elif a[i][0] == "?":
        b = [int(a[i][1]),int(a[i][2])]
        b.sort()
        if tate <= b[0] and yoko <= b[1]:
            print("YES")
        else:
            print("NO")
