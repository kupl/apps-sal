(a, b, c, d) = list(map(int, input().split()))
x = [0] * 101
cnt = 0
for i in range(a, b + 1):
    x[i] = 1
for i in range(c, d + 1):
    if x[i] == 1:
        cnt += 1
if cnt == 0:
    print(cnt)
else:
    print(cnt - 1)
