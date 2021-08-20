q = int(input())
for _ in range(q):
    (n, m, k) = list(map(int, input().split()))
    if max([n, m]) > k:
        print(-1)
    elif (n + m) % 2 == 0:
        if max([n, m]) % 2 != k % 2:
            print(k - 2)
        else:
            print(k)
    else:
        print(k - 1)
