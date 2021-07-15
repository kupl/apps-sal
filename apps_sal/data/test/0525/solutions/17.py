for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    x = arr.count(arr[0])
    if x==n:
        print(n)
    else:
        print(1)
