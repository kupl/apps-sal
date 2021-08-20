a = int(input())
for i in range(a):
    (n, k1, k2) = list(map(int, input().split()))
    k11 = list(map(int, input().split()))
    k22 = list(map(int, input().split()))
    if max(k11) > max(k22):
        print('YES')
    else:
        print('NO')
