a = [list(map(int, input().split())) for i in range(int(input()))]
n = len(a)
for i in range(n):
    for j in range(n):
        if a[i][j] != 1:
            found = False
            for i2 in range(n):
                for j2 in range(n):
                    if a[i][j] == a[i][j2] + a[i2][j]:
                        found = True
            if not found:
                print('No\n')
                return
print('Yes')
