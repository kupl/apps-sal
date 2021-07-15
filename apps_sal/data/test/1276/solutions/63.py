n = int(input())
s = input()

r = s.count("R")
g = s.count("G")
b = s.count("B")

ans = r * g * b
for i in range(n - 2):
    interval = 1
    while i + 2 * interval < n:
        if s[i] != s[i + interval] and s[i] != s[i + 2 * interval] and s[i + interval] != s[i + 2 * interval]:
            ans -= 1
        interval += 1

print(ans)
