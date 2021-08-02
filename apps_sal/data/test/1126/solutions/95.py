n, x, m = list(map(int, input().split()))

rem = [-1] * (m + 1)
rem[x] = 1
now = x
s = []

while True:
    s.append(now)
    next = (now * now) % m
    if rem[next] == -1:
        rem[next] = rem[now] + 1
    else:
        cycle_start = next
        break

    now = next


ans = 0
for i in range(rem[cycle_start] - 1):
    if n >= 1:
        n -= 1
        ans += s[i]
    else:
        break

cycle_sum = sum(s[rem[cycle_start] - 1:])
cycle_length = max(rem) - rem[cycle_start] + 1

ans += cycle_sum * (n // cycle_length)
n -= cycle_length * (n // cycle_length)

now = rem[cycle_start] - 1
while n > 0:
    ans += s[now]
    n -= 1
    now += 1

print(ans)
