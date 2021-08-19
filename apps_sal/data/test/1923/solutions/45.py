def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    res = sum((arr[i] for i in range(0, len(arr), 2)))
    print(res)


solve()
