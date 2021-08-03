n = int(input())
t = [0] * n
for _ in range(n - 1):
    a, b = input().split(' ')
    a, b = [int(a), int(b)]
    t[a - 1] += 1
    t[b - 1] += 1
out = [(e * (e - 1)) / 2 for e in t]
print(int(sum(out)))
