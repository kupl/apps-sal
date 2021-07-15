for _ in range(int(input())):
    n = int(input())
    ar1 = list(map(int, input().split()))
    ar2 = list(map(int, input().split()))
    ar1.sort()
    ar2.sort()
    print(*ar1)
    print(*ar2)
