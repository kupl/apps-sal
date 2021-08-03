for _ in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    V = [0, 0]
    for i in L:
        V[i % 2] += 1
    if V[0] == 0 or V[1] == 0:
        print('YES')
    else:
        print('NO')
