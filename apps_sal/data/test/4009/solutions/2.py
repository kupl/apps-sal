(n, x, y) = list(map(int, input().split()))
s = input()
s = s[::-1]
ans = 0
for i in range(x):
    if i == y:
        if s[i] == '0':
            ans += 1
    elif s[i] == '1':
        ans += 1
print(ans)
