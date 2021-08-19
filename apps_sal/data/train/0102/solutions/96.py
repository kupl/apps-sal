t = int(input())
for i in range(t):
    n = input()
    le = len(n)
    ans = 9 * (le - 1)
    l = n[0] * le
    if int(n) >= int(l):
        ans += int(n[0])
    else:
        ans += int(n[0]) - 1
    print(ans)
