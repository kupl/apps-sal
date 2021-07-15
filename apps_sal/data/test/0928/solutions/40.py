n, k = list(map(int, input().split()))
a_list = list(map(int, input().split()))

s = 0
t = 1
temp_sum = a_list[0]
ans = 0

while t <= n:
    if temp_sum >= k:
        temp_sum -= a_list[s]
        ans += n - t + 1
        s += 1

    else:
        if t >= n:
            break
        temp_sum += a_list[t]
        t += 1

print(ans)

