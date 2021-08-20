from sys import stdin
tt = int(stdin.readline())
for loop in range(tt):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    ans = 'NO'
    for i in range(n - 1):
        if a[i] <= a[i + 1]:
            ans = 'YES'
            break
    print(ans)
