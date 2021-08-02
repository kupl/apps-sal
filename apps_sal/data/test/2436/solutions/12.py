tt = int(input())

for loop in range(tt):

    n = int(input())

    a = list(map(int, input().split()))
    a.sort()

    ans = 1

    for i in range(n):
        if a[i] <= 1 + i:
            ans = i + 2
    print(ans)
