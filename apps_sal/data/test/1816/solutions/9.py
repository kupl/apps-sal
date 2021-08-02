n = int(input())

c = [0 for i in range(n)]

f = list([int(x) - 1 for x in input().split()])

for i in range(n):
    c[f[i]] = i

sum = 0
for i in range(n - 1):
    sum += abs(c[i] - c[i + 1])

print(sum)
