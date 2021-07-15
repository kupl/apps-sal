n = int(input())
up = 20000
ans = True
for i in range(n):
    le, dr = map(str, input().split())
    le = int(le)
    if ((up == 20000 and dr != "South") or (up == 0 and dr != "North")):
        ans = False
    else:
        if (dr == "South"):
            if (le > up):
                ans = False
            else:
                up -= le
        elif (dr == "North"):
            if (le > 20000 - up):
                ans = False
            else:
                up += le
if (up != 20000):
    ans = False
if (ans):
    print("YES")
else:
    print("NO")
