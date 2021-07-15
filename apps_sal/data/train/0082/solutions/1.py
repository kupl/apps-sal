for _ in range(int(input())):
    am = int(input())
    arr = list(map(int,input().split()))
    print(*list(reversed(arr)))
