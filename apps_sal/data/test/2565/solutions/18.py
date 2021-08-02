q = int(input())
for _ in range(q):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    myk = min(a[2], b[1])
    wyn = 0
    a[2] -= myk
    b[1] -= myk
    wyn += 2 * myk
    cyk = b[0] + b[1]
    dup = a[1]
    al = sum(a)
    wyn -= (max(0, dup - cyk)) * 2
    print(wyn)
