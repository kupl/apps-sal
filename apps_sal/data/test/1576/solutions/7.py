s = input()
ans = ""
n = len(s)
if n % 2 == 0:
    for i in range(1, n + 1):
        if i % 2 == 1:
            ans += s[- (i // 2 + 1)]
        else:
            ans += s[i // 2 - 1]
    print(ans[::-1])
else:
    for i in range(1, n + 1):
        if i % 2 == 1:
            ans += s[i // 2]
        else:
            ans += s[- (i // 2)]
    print(ans[::-1])
