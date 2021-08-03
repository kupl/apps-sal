t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = [i % 2 for i in a]
    if sum(c) == 0 or sum(c) == n:
        print('YES')
    else:
        print('NO')
