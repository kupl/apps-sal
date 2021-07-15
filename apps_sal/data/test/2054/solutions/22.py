for t in range(int(input())):
    n, k = list(map(int, input().split()))
    s = (n, k, (n+k)//3)
    print(min(s))

