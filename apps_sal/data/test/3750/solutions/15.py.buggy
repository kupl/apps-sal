k, a, b = list(map(int, input().split()))


if a == 0 and (b % k != 0):
    print(-1)
    return
if b == 0 and (a % k != 0):
    print(-1)
    return

time_a = (b >= k)
time_b = (a >= k)

if a % k != 0 and not time_a:
    print(-1)
    return
if b % k != 0 and not time_b:
    print(-1)
    return

print(a // k + b // k)
