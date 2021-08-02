T = int(input())
for t in range(T):
    a, b, c = list(map(int, input().split()))
    ans = a * ((c + 1) // 2) - b * (c // 2)
    print(ans)
