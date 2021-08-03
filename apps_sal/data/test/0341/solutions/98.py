n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = list(input())

if k < n:
    for i in range(k, n):
        if t[i] == t[i - k]:
            t[i] = "*"

print(p * t.count("r") + r * t.count("s") + s * t.count("p"))
