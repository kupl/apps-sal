def solve():
    n = int(input())
    arr = sorted(map(int, input().split()))
    print(arr[n] - arr[n-1])


for _ in range(int(input())):
    solve()

