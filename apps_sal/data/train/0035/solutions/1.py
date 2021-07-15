from sys import stdin
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    ans = 0
    arr = sorted(list(map(int,stdin.readline().split())))
    peo = 0
    for i in range(n):
        peo += 1
        if peo == arr[i]:
            ans += 1
            peo = 0
    print(ans)

