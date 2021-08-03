t, k = input(), int(input())
n = len(t)
s = min(k, (n + k) // 2)
for i in range(n - k):
    for j in range(i + s + 1, min(n, (n + i + k) // 2 + 1)):
        d = j - i
        if n - j > d:
            if t[i: j] == t[j: j + d]:
                s = d
        elif t[i: n - d] == t[j: n]:
            s = d
print(2 * s)
