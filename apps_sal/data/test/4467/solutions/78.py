n = int(input())
ab = [list(map(int,input().split())) for i in range(n)]
cd = [list(map(int,input().split())) for i in range(n)]

ab = sorted(ab, key=lambda x:(x[1], x[0]), reverse=True)
cd = sorted(cd, key=lambda x:(x[0], x[1]))

cnt = 0
i = j = 0
free_ab = [True] * n
while j < n:
    a, b = ab[i][0], ab[i][1]
    c, d = cd[j][0], cd[j][1]
    if a < c and b < d and free_ab[i]:
        cnt += 1
        free_ab[i] = False
        i = 0 
        j += 1
        continue
    elif j <= n-1 and i < n-1:
        i += 1
    elif j < n-1 and i == n-1:
        i = 0
        j += 1
    else:
        break
print(cnt)
