t = int(input())
for _ in range(t):
    (a, b) = list(map(int, input().split()))
    ans = (abs(a - b) + 9) // 10
    print(ans)
