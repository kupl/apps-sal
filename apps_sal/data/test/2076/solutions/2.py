from sys import stdin
n = int(stdin.readline().strip())
for i in range(n):
    a, b, c = list(map(int, stdin.readline().strip().split()))
    ans = 0
    while c >= 2 and b >= 1:
        c -= 2
        b -= 1
        ans += 3
    while b >= 2 and a >= 1:
        b -= 2
        a -= 1
        ans += 3
    print(ans)
