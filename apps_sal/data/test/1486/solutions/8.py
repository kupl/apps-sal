n = int(input())
l = list(map(int, input().split()))

left, right = l[0], l[n - 1]

for i in range(n):
    if i == 0:
        imin = abs(l[i] - l[i + 1])
    elif i == n - 1:
        imin = abs(l[i] - l[i - 1])
    else:
        imin = min(abs(l[i] - l[i - 1]), abs(l[i] - l[i + 1]))

    imax = max(abs(l[i] - left), abs(l[i] - right))

    print(imin, imax)
