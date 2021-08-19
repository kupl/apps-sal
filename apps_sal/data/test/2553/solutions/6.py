t = int(input())
for q in range(0, t):
    (n, x) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    a = 0
    for i in range(0, n):
        if arr[i] % 2 == 1:
            a += 1
    if a == n and x % 2 == 0:
        print('No')
    elif a == 0:
        print('No')
    elif x == n and a % 2 == 0:
        print('No')
    else:
        print('Yes')
