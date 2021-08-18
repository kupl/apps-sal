s = input()
n = int(s)

s = input()
x = s

ans = 0
for i in range(0, n):
    if x[i] == 'B':
        ans += 1 << i

print(ans)
