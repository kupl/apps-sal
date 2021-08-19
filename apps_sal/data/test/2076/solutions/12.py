t = int(input())
for i in range(t):
    (a, b, c) = map(int, input().split())
    ans = min(b, c // 2)
    b -= ans
    print(3 * (ans + min(a, b // 2)))
