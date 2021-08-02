t = int(input())
for i in range(t):
    x = int(input())
    ans = 0
    if x % 2 == 1:
        ans += 1
        x -= 3
    ans += x // 2
    print(ans)
