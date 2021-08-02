n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
a = 0
for i in range(k):
    l = "z"
    m = 0
    for c in t[i::k]:
        if c == l:
            m += 1
        else:
            if l == "r":
                a += p * (m // 2)
            elif l == "s":
                a += r * (m // 2)
            elif l == "p":
                a += s * (m // 2)
            l = c
            m = 2
    else:
        if l == "r":
            a += p * (m // 2)
        elif l == "s":
            a += r * (m // 2)
        elif l == "p":
            a += s * (m // 2)
print(a)
