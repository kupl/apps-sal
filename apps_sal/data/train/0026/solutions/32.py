t = int(input())

for case in range(t):
    n, m = map(int, input().split())
    ans = 'NO'
    if (n == m == 2):
        ans = 'YES'
    elif (n == 1 or m == 1):
        ans = 'YES'
    print(ans)
