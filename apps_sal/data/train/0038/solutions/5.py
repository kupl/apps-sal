t = int(input())
for rwuer in range(t):
    (n, k1, k2) = map(int, input().split())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    a1 = max(l1)
    a2 = max(l2)
    if a1 > a2:
        print('YES')
    else:
        print('NO')
