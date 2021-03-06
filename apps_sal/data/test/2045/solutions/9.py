def zalgo(s: str):
    l = 0
    r = 0
    n = len(s)
    z = [0] * n
    for i in range(1, n):
        z[i] = 0
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
        if i + z[i] == n:
            return z[i]
    return 0


n = int(input())
s = input().split()
txt = [s[0]]
for i in range(1, n):
    x = len(txt)
    y = len(s[i])
    mn = min(x, y)
    mx = zalgo(s[i] + '#' + ''.join(txt[-mn:]))
    txt.extend(s[i][mx:])
print(''.join(txt))
