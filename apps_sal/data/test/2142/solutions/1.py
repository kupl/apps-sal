t = int(input())
for _ in range(t):
    (n, m) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = -1
    for x in a:
        for y in b:
            if x == y:
                ans = x
    if ans != -1:
        print('YES')
        print(1, ans)
    else:
        print('NO')
