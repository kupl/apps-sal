s = [1] * 100001
s[0], s[1] = 0, 0
for i in range(2, 100001):
    if s[i] == 1:
        x = i * 2
        while x <= 100000:
            s[x] = 0
            x += i
ans = [0] * 100001
for i in range(3, 100001, 2):
    if s[i] == 1 and s[(i + 1) // 2] == 1:
        ans[i] = ans[i - 1] + 1
    else:
        ans[i] = ans[i - 1]
    ans[i + 1] = ans[i]
q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(ans[r] - ans[l - 1])
