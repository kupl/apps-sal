N = int(input())
a = list(map(int, input().split()))

# 箱に書かれた数字が大きい順にボールを入れるか決定していくとi以上のiの倍数
# についてはすでにボールを入れるか入れないかを決定している

ans = [0] * N
for i in range(N - 1, -1, -1):
    if (i == N - 1):
        if (a[i] == 0):
            continue
        else:
            ans[i] = 1
            continue

    elif (i == 0):
        sum_a = sum(ans)
    else:
        sum_a = sum(ans[i::(i + 1)])

    if (a[i] == 0 and sum_a % 2 == 0):
        continue
    elif(a[i] == 0 and sum_a % 2 == 1):
        ans[i] = 1
    elif (a[i] == 1 and sum_a % 2 == 0):
        ans[i] = 1
    elif (a[i] == 1 and sum_a % 2 == 1):
        continue
    else:
        print((-1))
        return

M = 0
new_ans = []
for i in range(N):
    if (ans[i] == 1):
        M += 1
        new_ans.append(i + 1)

if (M == 0):
    print(M)
    return
print(M)
print((*new_ans))
