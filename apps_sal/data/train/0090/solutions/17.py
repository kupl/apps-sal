for _ in range(int(input())):
    N = int(input())
    List = [int(x) for x in input().split()]
    Lock = [int(x) for x in input().split()]
    X = []
    for i in range(N):
        if(not Lock[i]):
            X.append(List[i])
    X.sort(reverse=True)
    j = 0
    for i in range(N):
        if(not Lock[i]):
            List[i] = X[j]
            j += 1
    print(*List)
