n = int(input())
s = input()
ans = 0
b = [0] * 50
b[0] = 1
for i in range(50):
    b[i] = 2 * b[i - 1] + 1
for i in range(n):
    if (s[i] == 'B'):
        ans += 1
        if (i > 0):
            ans += b[i - 1]
print(ans)
