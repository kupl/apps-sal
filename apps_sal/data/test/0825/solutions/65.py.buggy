import math
N = int(input())

if N == 1:
    print(0)
    return


def soinsu(m):
    arr = []
    temp = m
    for i in range(2, int(math.sqrt(m) + 1)):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([m, 1])

    return arr


arr = soinsu(N)
ans = 0
for i in range(len(arr)):
    s = 1
    con = arr[i][1]
    while con >= s:
        ans += 1
        con -= s
        s += 1
print(ans)
