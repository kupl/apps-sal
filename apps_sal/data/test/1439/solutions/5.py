n, m = (int(x) for x in input().split())
lst = [int(x) for x in input().split()]
cnt = [0 for i in range(m)]

if n > m:
    print("YES")
    return

for x in lst:
    cnt[x % m] += 1

tbl = [[False for j in range(n + 1)] for i in range(m)]

# print(tbl)

tbl[0][0] = True

for j in range(1, n + 1):
    for i in range(m):
        tbl[i][j] = tbl[i][j - 1]

    for i in range(m):
        #print(i, j)
        if tbl[i][j - 1]:
            if (i + lst[j - 1]) % m == 0:
                print("YES")
                return
            tbl[(i + lst[j - 1]) % m][j] = True

print("NO")
