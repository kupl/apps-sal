from math import gcd

n = int(input())
a = []
for i in range(n):
    row = input()
    a.append(bin(int(row,16))[2:].zfill(n))
# print(*a, sep='\n')
to_vis = [0]*n
ans = n
for i in range(n):
    br = False
    j = to_vis[i]
    while j < n:
        # print('j', j)
        currx = 1
        d = a[i][j]
        expand = True
        while expand and currx+i < n and currx+j < n:
            for ki in range(i, i+currx+1):
                if a[ki][j+currx] != d:
                    expand = False
                    break
            if expand:
                for kj in range(j, j+currx+1):
                    if a[i+currx][kj] != d:
                        expand = False
                        break
            if expand:
                currx += 1
        for ki in range(i, i+currx):
            if to_vis[ki] == j:
                to_vis[ki] = j+currx
        # print(currx)
        ans = gcd(ans, currx)
        if ans == 1:
            br = True
            break
        j += currx
        # print(to_vis)
    if br:
        break

print(ans)

