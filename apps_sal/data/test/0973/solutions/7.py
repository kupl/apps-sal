R,C = list(map(int , input().split()))
prev = input().replace('.', 'D')

res  = [prev]
for cnt in range(C-1):
    if (prev[cnt] == 'W' and prev[cnt+1] == 'S') or (prev[cnt] == 'S' and prev[cnt+1] == 'W'):
        print('No')
        return
for row in range(R-1):
    cur = input().replace('.', 'D')
    res.append(cur)
    if C==1 :
        if (prev[0] == 'W' and cur[0] == 'S') or (prev[0] == 'S' and cur[0] == 'W'):
            print('No')
            return

    for cnt in range(C-1):
        if (cur[cnt] == 'W' and cur[cnt+1] == 'S') or (cur[cnt] == 'S' and cur[cnt+1] == 'W'):
            print('No')
            return


    for cnt in range(C):
        if (prev[cnt] == 'W' and cur[cnt] == 'S') or (prev[cnt] == 'S' and cur[cnt] == 'W'):
            print('No')
            return

    prev = cur

print('Yes')
for c in res:
    print(c)


