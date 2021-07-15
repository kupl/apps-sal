N = int(input())
ans_max = 0
ans = 1
for i in range(1, N + 1):
    cnt = 0
    moto_i = i
    while i % 2 == 0:
        cnt += 1
        if cnt > ans_max:
            ans = moto_i
        ans_max = max(ans_max, cnt)
        i //= 2
print(ans)

