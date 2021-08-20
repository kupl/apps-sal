(N, K) = list(map(int, input().split()))
a = list(map(int, input().split()))
now = 0
ans = 0
position = 0
break_flag = 0
for i in range(N):
    while now < K:
        if position >= N:
            break_flag = 1
            break
        now += a[position]
        position += 1
    if break_flag == 1:
        break
    ans += N - position + 1
    now -= a[i]
print(ans)
