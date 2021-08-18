n = int(input())

l = list(range(1, n + 1))
a = []
target = (n * (n + 1)) // 4
accum = 0
for i in reversed(l):
    if accum + i <= target:
        a.append(i)
        accum += i

print(abs(accum - (n * (n + 1)) // 2 + accum))
print(len(a), ' '.join(str(x) for x in a))
