for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    kek = [0, 0]
    for x in arr:
        kek[x % 2] += 1
    print('YES' if kek[0] == 0 or kek[1] == 0 else 'NO')
