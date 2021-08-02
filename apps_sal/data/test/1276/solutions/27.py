n = int(input())
s = list(input())

cnt = 0
for j in range(2, n, 2):
    for i in range(0, n - j):
        k = (2 * i + j) // 2
        if s[i] != s[i + j] and s[i] != s[k] and s[k] != s[i + j]:
            cnt += 1

r, g, b = 0, 0, 0
for i in range(n):
    if s[i] == "R":
        r += 1
    elif s[i] == "G":
        g += 1
    else:
        b += 1

print(r * g * b - cnt)
