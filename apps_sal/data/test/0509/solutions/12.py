n = int(input())
a = [int(input()) for i in range(n)]
ok = [False for i in range(360)]
ok[0] = True

for i in range(n):
    ok2 = [False for i in range(360)]
    for j in range(360):
        if ok[j]:
            ok2[(j + a[i]) % 360] = True
            ok2[(j - a[i]) % 360] = True
    ok = ok2[:]

if ok[0]:
    print("YES")
else:
    print("NO")
