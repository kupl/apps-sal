s = input()

c = []
cur = s[0]
strk = 1
for i in range(1, len(s)):
    if s[i] == cur:
        strk += 1
    else:
        c.append((cur, strk))
        cur = s[i]
        strk = 1
c.append((cur, strk))

ans = [0] * len(s)
index = 0
for i in range(len(c)):
    even = c[i][1] // 2
    odd = c[i][1] - even

    if c[i][0] == "R":
        ans[index + c[i][1] - 1] += odd
        ans[index + c[i][1]] += even
    else:
        ans[index - 1] += even
        ans[index] += odd

    index += c[i][1]

print(" ".join(map(str, ans)))
