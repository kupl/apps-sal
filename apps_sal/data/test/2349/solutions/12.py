import math
t = int(input())
for i in range(t):
    n = int(input())
    m = math.floor(math.sqrt(n))
    ans = [j for j in range(m + 1)]
    left = m
    while m > 0:
        k = n // m
        if left == k:
            m -= 1
            continue
        ans.append(k)
        left = k
        m -= 1
    print(len(ans))
    print(*ans, sep=" ")
