t = int(input())
for z in range(t):
    a, b, c = list(map(int, input().split()))
    q, w = list(map(int, input().split()))
    if q >= w:
        print(q * min(a // 2, b) + min(max(0, (a - 2 * b)) // 2, c) * w)
    else:
        print(w * min(a // 2, c) + min(max(0, (a - 2 * c)) // 2, b) * q)

