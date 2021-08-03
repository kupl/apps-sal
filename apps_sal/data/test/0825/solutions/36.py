N = int(input())


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


ans = 0

soinsu_list = factorization(N)
# print(soinsu_list)
for i in range(len(soinsu_list)):
    cnt = 0
    while soinsu_list[i][0] != 1:
        cnt += 1
        soinsu_list[i][1] -= cnt
        if soinsu_list[i][1] < 0:
            cnt -= 1
            break
    ans += cnt
print(ans)
