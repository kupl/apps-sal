n, k = list(map(int, input().split()))
if n > k * (k - 1):
    print("NO")
else:
    count = 0
    diff = 1
    i = 0
    print("YES")
    while diff < k:
        while i < k and count < n:
            print("{} {}".format(i + 1, (i + diff) % k + 1))
            i += 1
            count += 1
        i = 0
        diff += 1
