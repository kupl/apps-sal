def solve():
    n = int(input())
    dots = [list(map(int, input().split())) for i in range(n)]
    dots.sort()
    for i in range(n - 1):
        if dots[i][1] > dots[i + 1][1]:
            print("NO")
            return
    x = 0
    y = 0
    ans = ""
    for i in dots:
        while x < i[0]:
            ans += "R"
            x += 1
        while y < i[1]:
            ans += "U"
            y += 1
    print("YES")
    print(ans)


t = int(input())
for jjj in range(t):
    solve()

