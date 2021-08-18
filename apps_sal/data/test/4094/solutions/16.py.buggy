k = int(input())
a = [0] * (10 ** 6 + 1)
a[0] = 7 % k
for i in range(k):
    a[i + 1] = (a[i] * 10 + 7) % k
for i in range(k):
    if a[i] == 0:
        print(i + 1)
        return
print(-1)
