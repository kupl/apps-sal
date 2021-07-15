t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    ans = 0
    while b >= 1 and c >= 2:
        ans += 3
        b -= 1
        c -= 2
    while b >= 2 and a >= 1:
        ans += 3
        b -= 2
        a -= 1
    print(ans)
