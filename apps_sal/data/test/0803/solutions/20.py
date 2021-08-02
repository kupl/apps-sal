n = int(input())
s = list(input())
a = s.count("x")
b = s.count("X")
c = "x" if a < b else "X"
k = abs(n // 2 - a)
print(k)
i = 0
while k > 0:
    if s[i] != c:
        s[i] = c
        k -= 1
    i += 1
print("".join(s))
