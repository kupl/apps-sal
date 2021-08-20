(n, k) = list(map(int, input().split()))
R = []
Ro = []
if k % 2 != 0:
    for i in range(1, n + 1):
        if i % k == 0:
            R.append(i)
    print(len(R) ** 3)
else:
    for i in range(1, n + 1):
        if i % k == 0:
            R.append(i)
        if i % k == k // 2:
            Ro.append(i)
    print(len(R) ** 3 + len(Ro) ** 3)
