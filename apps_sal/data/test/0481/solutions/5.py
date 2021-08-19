n, x = list(map(int, input().split()))
p = 0
for i in range(1, n + 1):
    if x % i == 0:
        k = x // i
        if k > n:
            continue
        p += 1
        # print(i,k)
print(p)
