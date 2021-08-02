N = int(input())

M = 10**9 + 7
s = 1
for i in range(1, N + 1):
    s *= i
    s %= M

print(s)
