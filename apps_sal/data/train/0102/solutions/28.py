t = int(input())
for i in range(0, t):
    n = input()
    ans = 9 * (len(n) - 1)
    if int(n) >= int(n[0] * len(n)):
        ans += int(n[0])
    else:
        ans += int(n[0]) - 1
    print(ans)
