t = int(input())

for _ in range(t):
    n, k1, k2 = list(map(int, input().strip().split()))
    prvi = list(map(int, input().strip().split()))
    drugi = list(map(int, input().strip().split()))

    if max(prvi) > max(drugi):
        print('YES')
    else:
        print('NO')
