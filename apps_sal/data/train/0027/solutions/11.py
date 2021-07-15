for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    dell = []
    for i in range(n):
        new = 0
        while A[i] % 2 != 1:
            A[i] //= 2
            new += 1
        dell.append([A[i], new])
    dicter = {}
    for el in dell:
        if el[1] > dicter.get(el[0], -1):
            dicter[el[0]] = el[1]
    ans = 0
    for el in dicter:
        ans += dicter[el]
    print(ans)
