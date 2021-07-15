for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    ar.sort()
    print(abs(ar[n] - ar[n - 1]))
