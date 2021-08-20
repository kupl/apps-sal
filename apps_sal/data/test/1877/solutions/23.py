N = int(input())
s = input()
now = 0
root = []
for c in s:
    if c == 'R':
        now += 1
    else:
        now -= 1
    root.append(now)
ans = 0
for i in range(1, N - 1):
    if root[i] == 0:
        if (root[i + 1] > 0) != (root[i - 1] > 0):
            ans += 1
print(ans)
