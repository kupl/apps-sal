n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = [_ for _ in str(input())]
ans = 0
for i in range(n):
    if i - k < 0:
        if t[i] == "r":
            ans += p
        elif t[i] == "s":
            ans += r
        elif t[i] == "p":
            ans += s
    else:
        if t[i] == "r" and t[i - k] != "r":
            ans += p
        elif t[i] == "s" and t[i - k] != "s":
            ans += r
        elif t[i] == "p" and t[i - k] != "p":
            ans += s
        else:
            t[i] = "a"
print(ans)
