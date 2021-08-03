n = int(input())
arr = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    p, x = list(map(int, input().split()))
    print((sum(arr[0:p - 1]) + sum(arr[p:]) + x))
