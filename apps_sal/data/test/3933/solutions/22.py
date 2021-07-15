n = int(input())
arr = list(map(int, input().split()))
if (len({arr[i + 1] - arr[i] for i in range(n - 1)}) == 1):
    print(arr[-1] + (arr[1] - arr[0]))
else:
    print(arr[-1])
