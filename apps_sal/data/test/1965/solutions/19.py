t = int(input())
for _ in range(t):
    n, x = list(map(int, input().split()))
    arr = [int(j) for j in input().split()]

    c = arr.count(x)
    if c == n:
        print(0)
        continue
    elif c > 0:
        print(1)
        continue

    net = 0
    for i in range(n):
        net += arr[i] - x

    if net == 0:
        print(1)
    else:
        print(2)
