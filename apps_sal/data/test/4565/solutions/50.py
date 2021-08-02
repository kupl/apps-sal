n = int(input())
s = input()

ans = [0] * (n + 1)
for i in range(n):
    if s[i] == 'E':
        ans[i + 1] = ans[i] + 1
    else:
        ans[i + 1] = ans[i]

print(min(i - ans[i] + ans[n] - ans[i + 1] for i in range(n)))
