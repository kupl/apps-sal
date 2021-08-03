n, k = map(int, input().split())
s = input()


def win(a, b):
    if a == b:
        return a
    return a if a + b in ["RS", "SP", "PR"] else b


shift = 1
for i in range(k):
    s1 = ""
    for j in range(n):
        x, y = s[j], s[(j + shift) % n]
        s1 += win(x, y)
    s = s1
    shift = shift * 2 % n

print(s[0])
