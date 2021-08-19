(n, q) = map(int, input().split())
arr = list(map(int, input().split()))
maximum = max(arr)
minimum = min(arr)
for i in range(q):
    t = int(input())
    if t >= minimum and t <= maximum:
        print('Yes')
    else:
        print('No')
