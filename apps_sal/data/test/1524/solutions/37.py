s = input()
n = len(s)
r = l = 0
point = -1

flag = 0
ans = [0] * n


for i in range(n):
    if (s[i] == 'R' and s[i + 1] == 'L'):
        r += 1
        point = i
        ans[point] += (r+1) // 2
        ans[point + 1] += (r) // 2
        r = l = 0
    elif s[i] == 'L' and (i == n-1 or s[i + 1] == 'R'):
        l += 1
        ans[point+1] += (l+1) // 2
        ans[point] += (l ) // 2
        l = r = 0
    elif s[i] == 'R':
        r += 1
        l = 0
    elif s[i] == 'L':
        l += 1
        r = 0

print((' '.join(map(str, ans))))

