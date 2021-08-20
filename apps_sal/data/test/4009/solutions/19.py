[n, x, y] = [int(i) for i in input().split()]
s = input()
t = ''
for i in range(x):
    t += s[len(s) - 1 - i]
ans = 0
for i in range(x):
    if y == i:
        ans += int(t[i] != '1')
    else:
        ans += int(t[i] != '0')
print(ans)
