n = int(input())
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            continue
        val = False
        for k in range(n):
            for l in range(n):
                if (a[i][k] + a[l][j] == a[i][j]):
                    val = True
        if val == False:
            print("No")
            return
print("Yes")
