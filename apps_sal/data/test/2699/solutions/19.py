t = int(input())
l = list(map(int, input().split()))
for i in range(t):
    a = 1
    k = 3
    for j in range(l[i]):
        print(a, end=" ")
        a = a + k
        k = k + k
    print()

    a = 2
    k = 3
    for j in range(l[i]):
        print(a, end=" ")
        a = a + k
        k = k + k
    print()

    a = 4
    k = 6
    for j in range(l[i]):
        print(a, end=" ")
        a = a + k
        k = k + k
    print()

    a = 3
    k = 3
    for j in range(l[i]):
        print(a, end=" ")
        a = a + k
        k = k + k
    print()
