for _ in range(int(input())):
    n = int(input())
    S = [d for d in map(int, input().split()) if d <= 2048]
    if sum(S) >= 2048:
        print('YES')
    else:
        print('NO')
