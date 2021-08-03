n = int(input())
ar = []
for i in range(n):
    ar.append(list(map(int, input().split())))
ar = list(sorted(ar))
if n == 1:
    print(1)
else:
    sum1 = 0
    ind = [0] * n
    r = ar[0][0]
    for i in range(1, n - 1):
        if ar[i][0] - ar[i][1] > max(r, ar[i - 1][0]):
            sum1 += 1
        elif ar[i][0] + ar[i][1] < ar[i + 1][0]:
            sum1 += 1
            r = max(r, ar[i][0] + ar[i][1])

    print(sum1 + 2)
