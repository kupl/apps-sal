(hour, minut) = map(int, input().split())
(h, d, c, n) = map(float, input().split())
time = hour * 60 + minut
ind = 0
ans = 100000000000000000000000000000000000000000000000000000
while time < 24 * 60:
    hungr = h + ind * d
    if time >= 20 * 60:
        price = c * 0.8
        if hungr % n == 0:
            a = hungr // n * price
        else:
            a = (hungr // n + 1) * price
    else:
        price = c * 1
        if hungr % n == 0:
            a = hungr // n * price
        else:
            a = (hungr // n + 1) * price
    if a < ans:
        ans = a
    time += 1
    ind += 1
print(ans)
