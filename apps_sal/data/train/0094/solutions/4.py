t = int(input())
for _ in range(t):
    (n, T) = map(int, input().split())
    l1 = [int(x) for x in input().split()]
    current = 0
    for i in range(n):
        if T % 2 == 0 and l1[i] == T // 2:
            if current:
                l1[i] = 0
                current = 0
            else:
                l1[i] = 1
                current = 1
        else:
            l1[i] = int(l1[i] > T // 2)
    print(*l1)
