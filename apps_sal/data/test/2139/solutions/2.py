s = input()
n = len(s)
ans = 0
lb = -1
for i in range(n - 3):
    if s[i:i + 4] == 'bear':
        left = i-lb
        right = n - 3 - i
        ans += left * right
        lb = i
print(ans)

