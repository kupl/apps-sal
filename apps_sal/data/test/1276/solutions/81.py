n = int(input())
s = input()

r = s.count("R")
g = s.count("G")
b = s.count("B")
rgb = r * g * b

for i in range(n - 1):
    for j in range(i + 1, n):
        k = 2 * j - i
        if k > n - 1 or s[i] == s[j] or s[i] == s[k] or s[j] == s[k]:
            continue
        rgb -= 1
print(rgb)
