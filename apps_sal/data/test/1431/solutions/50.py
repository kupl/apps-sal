N = int(input())
a = list(map(int, input().split()))

box = [-1] * (N + 1)
ball_in_list = []
for i in range(N, 0, -1):
    cnt = 0
    for j in range((N // i) * i, 2 * i - 1, -i):
        cnt += box[j]

    if cnt % 2 == a[i - 1]:
        box[i] = 0
    else:
        box[i] = 1
        ball_in_list.append(i)

print((len(ball_in_list)))
print((*ball_in_list))
