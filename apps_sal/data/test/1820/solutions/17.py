for _ in range(int(input())):
    n = int(input())
    u = list(map(int, input().split()))
    if u[0] + u[1] <= u[-1]:
        print(1, 2, n)
    else:
        print(-1)
    

