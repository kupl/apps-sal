t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    change = -1
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            change = i
            break
    if change == -1:

        print(-((-n) // 3))
        continue
    streak = 1
    ans = 0
    for i in range(change, change + n):
        if s[(i) % n] == s[(i + 1) % n]:
            streak += 1
        else:
            ans += streak // 3
            streak = 1
    ans += streak // 3
    print(ans)
