N, H = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort(key=lambda x: x[1], reverse=True)

a_max = 0
for i in range(N):
    a_max = max(a_max, AB[i][0])

cnt = 0
sum_throw = 0
for i in range(N):
    if AB[i][1] > a_max:
        sum_throw += AB[i][1]
        cnt += 1

        if sum_throw >= H:
            print(cnt)
            return


rem = H - sum_throw

q, r = divmod(rem, a_max)
if r == 0:
    cnt += q
else:
    cnt += q + 1

print(cnt)

