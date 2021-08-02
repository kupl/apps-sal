from collections import defaultdict

n = int(input())
x = defaultdict(int)
for i in range(n):
    s = input()
    x[s[0]] += 1

sol = 0
for i in x:
    a = x[i] // 2
    b = x[i] - a
    sol += a * (a - 1) // 2
    sol += b * (b - 1) // 2
print(sol)
