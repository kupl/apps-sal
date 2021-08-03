def funk():
    nonlocal m
    n, k = map(int, input().split())
    mass = [int(i) for i in input().split()]
    x = 0
    minn = 10 ** 9
    for i in range(n - k):
        q = mass[i]
        j = mass[i + k]
        if (j - q) < minn:
            minn, x = (j - q), (j + q) // 2
    m.append(x)


t = int(input())
m = []
for i in range(t):
    funk()

for i in m:
    print(i)
