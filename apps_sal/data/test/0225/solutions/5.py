a, b, c, d = list(map(int, input().split()))
arr = [a, b, c, d]
for i in range(2):
    for j in range(2):
        for z in range(2):
            for k in range(2):
                cnt = 0
                for l in range(4):
                    q = [i, j, z, k][l]
                    if q:
                        cnt += arr[l]
                    else:
                        cnt -= arr[l]
                if cnt == 0:
                    print('YES')
                    return
print('NO')

