tests = int(input())
while tests:
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr.reverse()
    for i in range(n):
        print(arr[i], end=' ')
    print()
    tests -= 1
