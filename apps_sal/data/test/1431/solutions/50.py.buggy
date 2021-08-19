N = int(input())
a = list(map(int, input().split()))

box = [-1] * (N + 1)
ball_in_list = []
# 箱について(i = N, N-1, ..., 1)
for i in range(N, 0, -1):
    cnt = 0
    # (N//i)*i, ..., 3*i, 2*i
    for j in range((N // i) * i, 2 * i - 1, -i):
        cnt += box[j]

    # 偶奇が同じならボールは入れない
    if cnt % 2 == a[i - 1]:
        box[i] = 0
    # 偶奇が異なる時、ボールを入れる、その行為を記録
    else:
        box[i] = 1
        ball_in_list.append(i)

print((len(ball_in_list)))
print((*ball_in_list))
