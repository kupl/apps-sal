H = int(input())
N = 0
while True:
    N += 1
    if 2 ** N > H:
        break
a = [1] * N
for i in range(N):
    if i == 0:
        a[i] = 1
    else:
        a[i] = 2 * a[i - 1] + 1
print(a[-1])
