n = int(input())
s = input()
r, g, b = [], [], []

for i in range(n):
    if s[i] == "R":
        r.append(i)
    elif s[i] == "G":
        g.append(i)
    elif s[i] == "B":
        b.append(i)
ans = len(r) * len(g) * len(b)

for i in range(n):
    for j in range(i + 1, n):
        k = j + j - i
        if k < n:
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
print(ans)
