(n, k) = map(int, input().split())
r = 0
m = 0
for i in input().split():
    a = int(i) + m
    if a < k:
        if m != 0:
            r += 1
            m = 0
        else:
            m = a
    else:
        r += a // k
        m = a % k
r += (m + k - 1) // k
print(r)
