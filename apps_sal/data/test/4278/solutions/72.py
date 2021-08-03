n = int(input())
s = sorted([sorted(input()) for _ in range(n)])
ans = 0
x = 0
i = 0
while x < n - 1:
    cnt = 1
    for i in range(x, n - 1):
        if s[i] == s[i + 1]:
            cnt += 1
            x = i + 1
        else:
            x = i + 1
            break
    ans += (cnt * (cnt - 1)) / 2
print(int(ans))
