n = int(input())
arr = [0] * (n + 1)
for i in range(1, n + 1):
    x = []
    while i % 2 == 0:
        x.append(2)
        i = i // 2
    f = 3
    while f * f <= i:
        if i % f == 0:
            x.append(f)
            i = i // f
        else:
            f += 2
    if i != 1:
        x.append(i)
    for k in range(len(x)):
        arr[x[k]] += 1
ans = 1
for i in range(len(arr)):
    ans *= arr[i] + 1
print(ans % (10 ** 9 + 7))
