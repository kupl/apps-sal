N, X, M = list(map(int, input().split()))
dic = {}
a = X
dic[X] = 1
seen = set([a])
roop_length = 0
roop_start = 0
ans = X
for i in range(2, N + 1):
    a = pow(a, 2, M)
    if a in seen:
        roop_length = i - dic[a]
        roop_start = dic[a]
        roop_start_a = a

        break
    else:
        ans += a
        seen.add(a)
        dic[a] = i
roop_ans = 0
if roop_length > 0:
    roop_ans = roop_start_a
    a = roop_start_a
    for i in range(1, N + 1):
        a = pow(a, 2, M)
        if a != roop_start_a:
            roop_ans += a
        else:
            break
    roop_ans = roop_ans * ((N - roop_start + 1) // roop_length - 1)

rest_ans = 0
if roop_length > 0:
    rest_num = (N - roop_start + 1) % roop_length
    rest_ans = roop_start_a * (rest_num > 0)
    a = roop_start_a
    for _ in range(1, rest_num):
        a = pow(a, 2, M)
        rest_ans += a

ans_all = ans + roop_ans + rest_ans
print(ans_all)
