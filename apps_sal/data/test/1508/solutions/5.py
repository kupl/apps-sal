a = int(input())
arr = list(map(int, input().split()))
if(a == 2):
    print(*(sorted(arr)[::-1]))
else:
    arr = sorted(arr)[::-1]
    arr[1:-1] = sorted(arr[1:-1])
    print(*arr)
