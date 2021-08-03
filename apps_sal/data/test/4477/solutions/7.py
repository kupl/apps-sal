t = int(input())
for _ in range(t):
    x = input()
    ans = 0
    ans += (int(x[0]) - 1) * 10
    ans += len(x) * (len(x) + 1) // 2
    print(ans)
