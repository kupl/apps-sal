n = int(input())
(c, s, f) = ([], [], [])
for _ in range(n - 1):
    (x, y, z) = map(int, input().split())
    c.append(x)
    s.append(y)
    f.append(z)
for i in range(n - 1):
    temp = s[i] + c[i]
    for j in range(i + 1, n - 1):
        if temp <= s[j]:
            temp = s[j] + c[j]
        elif (temp - s[j]) % f[j] == 0:
            temp += c[j]
        else:
            k = (temp - s[j]) // f[j] + 1
            temp = s[j] + k * f[j] + c[j]
    print(temp)
print(0)
