(t, s, q) = [int(i) for i in input().split()]
c = (q - 1) / q
cnt = 1
time = s
while True:
    time = time / (1 - c)
    if t - time <= 0.0001:
        break
    cnt += 1
print(cnt)
