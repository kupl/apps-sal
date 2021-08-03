def nod(a, b):
    for i in range(min(a, b), 0, -1):
        if (a % i == 0 and b % i == 0):
            return i


def nok(a, b):
    return a * b // nod(a, b)


n = int(input())
m = [int(x) for x in input().split()]
r = [int(x) for x in input().split()]
ans = 1
for i in range(n):
    ans = nok(ans, m[i])

x = 0
for d in range(ans):
    for i in range(n):
        if d % m[i] == r[i]:
            x += 1
            break
print(x / ans)
