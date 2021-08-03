n = int(input())
s = 0
for i in range(n):
    s += (n - i) * (i + 1) - i

print(s)
