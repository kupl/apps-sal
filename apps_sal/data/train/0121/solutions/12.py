for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    l1.sort()
    print(l1[n] - l1[n-1])

