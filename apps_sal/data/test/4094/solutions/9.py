k = int(input())
a = [0] * (10 ** 6 + 1)
a[1] = 7 % k
for i in range(2, k + 1):
    a[i] = (a[i - 1] * 10 + 7) % k
for i in range(1, k + 1):
    if a[i] == 0:
        print(i)
        break
else:
    print(-1)
