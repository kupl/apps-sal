n, x, m = map(int, input().split())


def A(x, m):
    return (x**2) % m


now = x
ans = 0
streak = []
used = set()
loop = False
while n > 0:
    if now in used:
        loop = True
        break
    used.add(now)
    ans += now
    streak.append(now)
    now = A(now, m)
    n -= 1

if loop:
    loop_sum = 0
    loop_streak = []
    for j, item in enumerate(streak[::-1]):
        loop_sum += item
        loop_streak.append(item)
        if item == now:
            loop_length = j + 1
            break
    ans += (n // loop_length) * loop_sum
    loop_streak.reverse()
    ans += sum(loop_streak[:n % loop_length])

print(ans)
