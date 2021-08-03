def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if not arr[i]:
            arr[i] += 1
            cnt += 1
    if not sum(arr):
        cnt += 1
    return cnt


for _ in range(int(input())):
    print(solve())
