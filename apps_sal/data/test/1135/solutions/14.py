n = int(input())
s = input()
ans = ''
for i in range(n - 1, -1, -1):
    ans = ans[:(n - i) // 2] + s[i] + ans[(n - i) // 2:]
ans2 = ''
for i in range(n - 1, -1, -1):
    ans2 += ans[i]
print(ans2)
