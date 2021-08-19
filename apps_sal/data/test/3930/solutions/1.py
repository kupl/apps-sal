from sys import stdin, stdout
(n, k) = map(int, stdin.readline().split())
values = list(map(int, stdin.readline().split()))
cnt = [0]
d = {0: 1}
power = [1]
ans = 0
if abs(k) > 1:
    while abs(power[-1]) < 10 ** 16:
        power.append(power[-1] * k)
elif k == -1:
    power = [1, -1]
elif not k:
    power = [0]
for i in range(n):
    cnt.append(cnt[-1] + values[i])
    if cnt[-1] in d:
        d[cnt[-1]] += 1
    else:
        d[cnt[-1]] = 1
    for v in power:
        if cnt[-1] - v in d:
            ans += d[cnt[-1] - v]
stdout.write(str(ans))
