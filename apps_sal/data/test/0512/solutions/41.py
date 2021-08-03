N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

judge = True
flag = [0] * 201

for i in AB:
    if i[0] == -1:
        if i[1] != -1:
            if flag[i[1]]:
                judge = False
            else:
                flag[i[1]] = i
    else:
        if i[1] == -1:
            if flag[i[0]]:
                judge = False
            else:
                flag[i[0]] = i
        else:
            if (flag[i[0]]) or (flag[i[1]]):
                judge = False
            else:
                if i[0] >= i[1]:
                    judge = False
                else:
                    flag[i[0]] = i
                    flag[i[1]] = i

dp = [0] * (2 * N + 1)
dp[0] = 1
for left in range(1, 2 * N, 2):
    for right in range(left + 1, 2 * N + 1, 2):
        length = (right - left + 1) // 2
        for i in range(left, left + length):
            x = flag[i]
            if x:
                if (x[0] != -1) and (x[1] != -1) and (x[1] - x[0] != length):
                    break
                elif (x[0] == -1):
                    break
                elif (x[1] == -1) and (flag[i + length]):
                    break
                elif (x[1] == i):
                    break

            else:
                if (flag[i + length]) and (flag[i + length][0] != -1) and (flag[i + length][0] != i):
                    break

        else:
            if dp[left - 1]:
                dp[right] = 1

if judge and dp[-1]:
    print('Yes')
else:
    print('No')
