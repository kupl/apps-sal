q = int(input())
for i in range(q):
    n = int(input())
    p = list(map(int, input().split()))
    for i in range(n - 1):
        if p[i] + 1 != p[i + 1] and (not (p[i] == n and p[i + 1] == 1)):
            break
    else:
        print('YES')
        continue
    for i in range(n - 1):
        if p[i] - 1 != p[i + 1] and (not (p[i] == 1 and p[i + 1] == n)):
            break
    else:
        print('YES')
        continue
    print('NO')
