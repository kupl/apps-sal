def resolve():
    n = int(input())
    p = map(int, input().split())
    cnt = 0
    for (i, j) in enumerate(p):
        if i + 1 != j:
            cnt += 1
    print('YES' if cnt < 3 else 'NO')


resolve()
