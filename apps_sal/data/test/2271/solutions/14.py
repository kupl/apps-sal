n = int(input())
t = [0] * n
out = 0
for _ in range(n - 1):
    a, b = input().split(' ')
    a, b = [int(a), int(b)]
    t[a - 1] += 1
    t[b - 1] += 1
for x in t:
    out += x * (x - 1) / 2
print(int(out))
