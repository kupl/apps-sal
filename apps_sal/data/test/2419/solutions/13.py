t = int(input())
for _ in range(t):
    (a, b) = list(map(int, input().split()))
    m = int((abs(b - a) * 2) ** 0.5)
    for i in range(10):
        q = m * (m + 1) // 2
        if q >= abs(b - a) and (q - abs(b - a)) % 2 == 0:
            print(m)
            break
        m += 1
