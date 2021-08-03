n = int(input())
s = input()
ans = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        m = {'L': 0, 'R': 0, 'U': 0, 'D': 0}
        s1 = s[i:j + 1]
        for x in s1:
            m[x] += 1
        if m['L'] == m['R'] and m['U'] == m['D']:
            ans += 1
print(ans)
