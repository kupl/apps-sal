t = int(input())
for _ in range(t):
    (n, k1, k2) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if max(a) > max(b):
        print('YES')
    else:
        print('NO')
