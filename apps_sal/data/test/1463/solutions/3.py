n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
ok = True
for i in range(n):
    for j in range(n):
        if a[i][j] != 1:
            check = False
            for k in range(n):
                for l in range(n):
                    if a[i][j] == a[i][k] + a[l][j]:
                        check = True
                    if check:
                        break
                if check:
                    break
            ok &= check
print("Yes" if ok else "No")
